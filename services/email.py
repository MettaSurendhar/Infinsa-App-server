import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up email details from environment variables
sender_email="example@gmail.com"
password="password"
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Define the receiver email
receiver_email = "receivermail@gamil.com"

subject = "Won Lucky Prize"

# HTML content
html_content = """
<html>
  <body>
    <p>Security check mail</p>
  </body>
</html>
"""

# Create the email message
message = MIMEMultipart("alternative")
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the plain text and HTML parts to the message
html_part = MIMEText(html_content, "html")

message.attach(html_part)

# Establish a connection to the SMTP server and send the email
try:
    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, password)  # Log in to the SMTP server
        server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email
    print("Email sent successfully")
except Exception as e:
    print(f"Error: {e}")
