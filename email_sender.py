import smtplib
import ssl
from email.message import EmailMessage


def send_email(
    message: str,
    subject: str,
    host: str,
    username: str,
    password: str,
    receiver: str,
    nasa_apod: bytes,
):
    """
    Sends an email using EmailMessage with a plain-text body and one image attachment.

    Parameters:
        - message: The plain-text message body.
        - subject: The subject of the email.
        - host: SMTP server host (e.g. 'smtp.gmail.com').
        - username: Email account username.
        - password: Email account password.
        - receiver: Recipient email address.
        - nasa_apod: Raw bytes of the image to attach (e.g. requests.get(url).content).
    Output:
        - Email sent
    """
    PORT = 465
    CONTEXT = ssl.create_default_context()

    # Create an EmailMessage object
    msg = EmailMessage()
    msg["From"] = username
    msg["To"] = receiver
    msg["Subject"] = subject

    # Set the plain-text content
    msg.set_content(message)

    # Attach the image (APOD) as bytes
    # Make sure nasa_apod contains the raw image bytes
    msg.add_attachment(
        nasa_apod,
        maintype="image",
        subtype="jpeg",  # or 'png', depending on actual format
        filename="apod.jpg",
    )

    # Connect to SMTP server and send
    with smtplib.SMTP_SSL(host, PORT, context=CONTEXT) as server:
        server.login(username, password)
        server.send_message(msg)
