import schedule
import time
from django.utils import timezone
# from models import SentMessage
from tele_bot_project.tele_bot_app.models.models_sentmessage import SentMessage


def send_schedule_message():
    pass

schedule.every().day.at("10:00").do(send_schedule_message)

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(5)

run_schedule()