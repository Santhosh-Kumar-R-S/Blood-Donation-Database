from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = 'xyz'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'blood_donation_db'

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'example@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'abcd efgh ijkl mnop'  # Replace with your email password 

mail = Mail(app)

# Database Connection
db = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)
cursor = db.cursor()

@app.route('/')
def index():
    # Fetch all donors from the database
    cursor.execute("SELECT * FROM Donors")
    donors = cursor.fetchall()
    return render_template('index.html', donors=donors)

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        donor_name = request.form['donor_name']
        blood_group = request.form['blood_group']
        location = request.form['location']
        email = request.form['email']
        mobile_number = request.form['mobile_number']

        # Insert into Donors table
        cursor.execute("INSERT INTO Donors (donor_name, blood_group, location, email, mobile_number) VALUES (%s, %s, %s, %s, %s)", 
                       (donor_name, blood_group, location, email, mobile_number))
        
        # Insert into Users table
        cursor.execute("INSERT INTO Users (username, email, password) VALUES (%s, %s, %s)", 
                       (donor_name, email, 'default_password'))  # Replace 'default_password' with a secure password
        
        # Update BloodAvailable table
        cursor.execute("SELECT * FROM BloodAvailable WHERE blood_group = %s", (blood_group,))
        blood_available = cursor.fetchone()

        if blood_available:
            new_quantity = blood_available[2] + 1  # Increment quantity by 1
            cursor.execute("UPDATE BloodAvailable SET quantity = %s WHERE blood_id = %s", 
                           (new_quantity, blood_available[0]))
        else:
            cursor.execute("INSERT INTO BloodAvailable (blood_group, quantity) VALUES (%s, %s)", 
                           (blood_group, 1))  # Start with quantity 1
        
        db.commit()
        flash('Thank you for your donation!', 'success')
        return redirect(url_for('index'))

    return render_template('donate.html')

@app.route('/request/<int:donor_id>', methods=['GET', 'POST'])
def request_blood(donor_id):
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        blood_group_needed = request.form['blood_group_needed']
        email = request.form['email']
        contact_number = request.form['contact_number']

        # Fetch donor details
        cursor.execute("SELECT * FROM Donors WHERE donor_id = %s", (donor_id,))
        donor = cursor.fetchone()

        if donor:
            # Insert into Requests table
            cursor.execute("INSERT INTO Requests (patient_name, blood_group_needed, email) VALUES (%s, %s, %s)", 
                           (patient_name, blood_group_needed, email))
            
            # Send email to the donor
            msg = Message('Blood Request', 
                          sender=app.config['MAIL_USERNAME'], 
                          recipients=[donor[4]])  # donor[4] is the donor's email
            msg.body = f"Dear {donor[1]},\n\n{patient_name} has requested {blood_group_needed} blood.\n\nContact them at {email} or {contact_number}."
            mail.send(msg)

            # Log the email in the Emails table
            cursor.execute("INSERT INTO Emails (recipient_email, subject, body) VALUES (%s, %s, %s)", 
                           (donor[4], 'Blood Request', msg.body))
            
            db.commit()
            flash('Request sent successfully!', 'success')
        else:
            flash('Donor not found.', 'danger')

        return redirect(url_for('index'))

    return render_template('request.html', donor_id=donor_id)

if __name__ == '__main__':
    app.run(debug=True)
