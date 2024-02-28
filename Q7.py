import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, recipient_emails, subject, body):
   
    smtp_server = "smtp.mailtrap.io"
    smtp_port = 2525
    smtp_username = "521a3608c78720"
    smtp_password = "a4f9dba122bc3e"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ", ".join(recipient_emails)
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, recipient_emails, message.as_string())
        print("Email sent successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

sender_email = input("Enter sender email address:")

num_recipients = int(input("Enter number of recipients: "))
recipient_emails = []

for i in range(num_recipients):
    recipient_email = input(f"Enter email address for recipient {i + 1}: ")
    recipient_emails.append(recipient_email)

subject = input("Enter the email subject: ")
body = input("Enter the email body: ")

send_email(sender_email, recipient_emails, subject, body)
