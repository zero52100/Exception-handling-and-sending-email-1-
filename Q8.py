import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = input("Enter sender email address: ")
recipient_email = input("Enter recipient's email address: ")
subject = input("Enter email subject: ")
body = input("Enter email body: ")

smtp_server = "smtp.mailtrap.io"
smtp_port = 2525
smtp_username = "521a3608c78720"
smtp_password = "a4f9dba122bc3e"

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
    print("Email sent successfully.")

except smtplib.SMTPException as e:
    if isinstance(e, smtplib.SMTPAuthenticationError):
        print("Authentication error. Check your username and password.")
    else:
        print(f"SMTP error occurred: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
