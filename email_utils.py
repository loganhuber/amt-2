import os
import smtplib
from dotenv import load_dotenv
from datetime import datetime
from dataclasses import dataclass
from email.message import EmailMessage

load_dotenv()

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

class EmailSendError(Exception):
    pass

@dataclass
class OutgoingMail:
    to: str
    subject: str
    body: str


def build_email(user_email, name, message):

    email = OutgoingMail(
        to=EMAIL_ADDRESS,
        subject=f"New Message from amammothtask.com",
        body=(
            f"Name: {name}\n"
            f"Email: {user_email}\n"
            f"Message: {message}"
        )
    )

    return email


def send_email(email: OutgoingMail):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
            raise RuntimeError("Error: Email or Password not set")
        
        msg = EmailMessage()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = email.to
        msg["Subject"] = email.subject
        msg.set_content(email.body)

        try:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        except smtplib.SMTPException as e:
            raise EmailSendError("SMTP Failed") from e
        