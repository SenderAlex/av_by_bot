
from celery import shared_task
from django.conf import settings
import requests
# from .models import MessageData
from tele_bot_project.tele_bot_app.models.models_messagedata import MessageData


@shared_task
def send_scheduled_message_task():
    token = settings.TOKEN
    message = "Ваше автоматически отправленное сообщение"

    queryset = MessageData.objects.all()  # нужно вставить требуемую модель
    for obj in queryset:
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={obj.telegram_id}&text={message}"
        requests.get(url).json()


# необходимо запустить следующие команды
# celery -A tele_bot_project worker --beat --scheduler django --loglevel=info
# celery -A tele_bot_project worker -l info
# celery -A tele_bot_project beat -l info
