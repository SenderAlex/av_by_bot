import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tele_bot_project.settings')  # tele_bot_project.settings  21.03.2024

app = Celery('tele_bot_project')  # tele_bot_project  21.03.2024
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'get_categories_every_one_minutes': {
        'task': 'src.main.tasks.get_api',
        'schedule': crontab(minute='*/1')
    },
}



# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')