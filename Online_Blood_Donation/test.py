import smtplib
from email.mime.text import MIMEText

# Email details
sender = 'samshasadwin@gmail.com'
receiver = 'samsadwin@gmail.com'
password = 'xegl kert wnjv bqsl'

# Create the email
msg = MIMEText('This is a test email.')
msg['Subject'] = 'Test Email'
msg['From'] = sender
msg['To'] = receiver

# Send the email
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Enable TLS encryption
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError as e:
    print(f"Failed to send email: {e}")