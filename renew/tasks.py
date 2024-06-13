from io import BytesIO
from django.conf import settings
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .models import CallMe


@shared_task
def send_email_task(first_name):
    try:
        send_mail('New CallMe Request',
                  f'Hi, {first_name}!',
                  settings.EMAIL_HOST_USER,
                  ['renovatsia-tech@yandex.ru'],
                  fail_silently=False,
                  html_message=render_to_string('email.html', {'first_name': first_name})
        )
        logging.info("Mail to manager sent successfully")
    except Exception as e:
        logging.error(f"Error sending mail: {str(e)}")