from pydantic import EmailStr
import smtplib

from app.config import settings
from app.tasks.background_tasks import celery_app
from app.tasks.email_templates import create_booking_confirmation_template

@celery_app.task
def process_pic(path: str):
    pass


@celery_app.task
def send_confirmation_email(
        email_to: EmailStr
):
    email_to_mock = settings.SMTP_USER
    msg_content = create_booking_confirmation_template(email_to)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)
