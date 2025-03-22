import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(
    message: str, subject: str, host: str, username: str, password: str, receiver: str
):
    # Inputs
    PORT = 465
    CONTEXT = ssl.create_default_context()

    # Create a MIMEMultipart object and add headers
    msg = MIMEMultipart()
    msg["From"] = username
    msg["To"] = receiver
    msg["Subject"] = subject

    # Attach the message body, specifying 'plain' text and UTF-8 encoding
    msg.attach(MIMEText(message, "plain", "utf-8"))

    with smtplib.SMTP_SSL(host, PORT, context=CONTEXT) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg.as_string())
