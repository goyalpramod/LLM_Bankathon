# IMPORTANT - THIS SCRIPT WILL NOT WORK ON COLLEGE FIREWALL BECAUSE PORT BLOCKED

import smtplib
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
email_pass = os.getenv("MAIL_PASSWORD")
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('crusherscode0@gmail.com', email_pass)
server.sendmail('crusherscode0@gmail.com', 'goyalpramod1729@gmail.com', 'hey')
print("mail sent")

# def send_email(sender_email, sender_password, receiver_email, message):
#     try:
#         smtp_server = 'smtp.example.com'  # Replace with your SMTP server address
#         smtp_port = 587  # Replace with your SMTP server port
#
#         # Establish a connection to the SMTP server
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()  # Upgrade the connection to a secure SSL/TLS connection
#         server.login(sender_email, sender_password)  # Log in to the SMTP server
#
#         # Send the email
#         server.sendmail(sender_email, receiver_email, message)
#
#         # Close the connection to the SMTP server
#         server.quit()
#
#         print("Email sent successfully!")
#     except Exception as e:
#         print("Failed to send email:", e)
#
# send_email('crusherscode0@gmail.com')
