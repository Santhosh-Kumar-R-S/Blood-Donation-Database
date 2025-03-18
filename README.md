# Online Blood Donation System

The **Online Blood Donation System** is a web-based platform designed to connect blood donors with recipients in need. The system allows donors to register their details, and recipients can request blood based on their requirements. The platform also includes features like blood availability tracking and automated email notifications to facilitate seamless communication between donors and recipients.

---

## Features

- **Donor Registration**: Donors can register by providing their details, including name, blood group, location, email, and contact information.
- **Blood Request**: Recipients can request blood by specifying the required blood group. The system matches donors and sends automated email notifications.
- **Blood Availability Tracker**: Tracks the quantity of available blood groups in real-time.
- **Email Notifications**: Automatically sends emails to donors when a request is made.
- **User-Friendly Interface**: Easy-to-use web interface for both donors and recipients.

---

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript
- **Email Notifications**: Flask-Mail
- **QR Code Generation**: `qrcode` library (for donor/recipient identification)

---

## Installation and Setup

### Prerequisites

1. **Python 3.x**: Install Python from [python.org](https://www.python.org/).
2. **MySQL**: Install MySQL from [mysql.com](https://www.mysql.com/).
3. **Flask**: Install Flask using pip:
   ```bash
   pip install Flask
   ```
4. **Flask-Mail**: Install Flask-Mail for email notifications:
   ```bash
   pip install Flask-Mail
   ```
5. **MySQL Connector**: Install the MySQL connector for Python:
   ```bash
   pip install mysql-connector-python
   ```

## Steps to Run the Project

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/online-blood-donation.git
    cd online-blood-donation
   ```
2. **Set Up the Database**:

    Create a MySQL database named `blood_donation_db`.

    Run the `database.sql` script to create the required tables:
    ```bash
   mysql -u root -p blood_donation_db < database.sql
   ```
3. **Configure Environment Variables**:

    Create a `.env` file in the project root and add the following variables:

    ```bash
    MYSQL_HOST=localhost
    MYSQL_USER=root
    MYSQL_PASSWORD=your_password
    MYSQL_DB=blood_donation_db
    MAIL_USERNAME=your_email@gmail.com
    MAIL_PASSWORD=your_email_password
    ```

4. **Run the Application**:
     ```bash
     python app.py
     ```
     The application will start at `http://127.0.0.1:5000`.

## Project Structure

```bash
online-blood-donation/
│── app.py                # Main Flask backend code
│── config.py             # Flask configuration (DB & settings)
│── requirements.txt      # Python dependencies
│── database.sql          # SQL file for table creation
│── templates/            # Folder for HTML files
│   ├── index.html        # Home page template
│   ├── request.html      # Blood request page template
│   ├── donate.html       # Blood donation page template
│── static/               # Folder for static files (CSS, JS, Images)
│   ├── css/              # Folder for CSS files
│   │   └── style.css     # Main CSS file
│   ├── js/               # Folder for JavaScript files
│   │   └── script.js     # JavaScript file (optional)
```

## Usage

1. **Home Page**:

    - Visit `http://127.0.0.1:5000` to access the home page.

   - View the list of registered donors and their details.

2. **Donate Blood**:

    - Click on the "Donate Blood" link to register as a donor.

    - Fill out the form with your details and submit.

3. Request Blood:

    - Click on the "Request" button next to a donor's name.

    - Fill out the request form with the patient's details and submit.

    - The system will send an email to the donor with the request details.
