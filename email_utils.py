import smtplib
from datetime import datetime
from dataclasses import dataclass
from email.message import EmailMessage
from flask import current_app


class EmailSendError(Exception):
    pass

@dataclass
class OutgoingMail:
    to: str
    subject: str
    body: str


def build_email(user_email, name, message):

    EMAIL_ADDRESS = current_app.config['EMAIL_ADDRESS']

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

        EMAIL_ADDRESS = current_app.config['EMAIL_ADDRESS']
        EMAIL_PASSWORD = current_app.config['EMAIL_PASSWORD']

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
        