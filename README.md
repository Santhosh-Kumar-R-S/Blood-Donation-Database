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
    MAIL_PASSWORD=your_email_app_password
    ```

    detailed note for creating the `mail_app_password` [Click Here](https://drive.google.com/file/d/1iM7bAg4cJGCOi4VQZTiAVRONf9fq7ZCL/view?usp=drivesdk)

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

## Screenshots
   ### 1. Home Page 
   ![Home Page](https://github.com/user-attachments/assets/3e5e7856-2807-4875-8118-31d6f9277ab5)

   ### 2. Donate Blood
   ![Donate Blood](https://github.com/user-attachments/assets/74fe2675-38a4-4c59-a4e5-4bb9c8917c43)

   ### 3. Request Blood
   ![Blood Request](https://github.com/user-attachments/assets/b637553d-47a2-4c5b-965e-6a172a72c2f5)


   ### 4. Blood Request Mail sent over to the Donar 
   
   ![Blood Request Mail Sent](https://github.com/user-attachments/assets/e8febf8b-5bbb-4a68-b282-6adb2eef8be0)

## Future Enhancements
   - Real-Time Notifications: Integrate SMS or mobile app notifications for faster communication.

   - Geolocation-Based Search: Allow recipients to search for donors within a specific radius.

   - Machine Learning: Predict blood demand based on historical data.

   - Admin Panel: Add an admin interface to manage donors, requests, and blood inventory.


## Contributors

We would like to thank the following contributors for their valuable contributions to this project:

- **[Santhosh Kumar R S](https://github.com/Santhosh-Kumar-R-S)** - Project Lead, Backend Development, Frontend Development, Database Design
- **[Shalom Joshua L](https://github.com/Shalom-Joshua-L)** - Frontend Development, Testing and Documentation

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
   - Fork the repository.
   - Create a new branch for your feature or bugfix.
   - Commit your changes and push to the branch.
   - Submit a pull request.

     
## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/Santhosh-Kumar-R-S/Blood-Donation-Database/blob/main/LICENSE) file for details.


## Contact
For any questions or feedback, please contact:

   - Santhosh Kumar R S

   - Email: snthshkumarrs@gmail.com

   - GitHub: [Santhosh-Kumar-R-S](https://github.com/Santhosh-Kumar-R-S)

