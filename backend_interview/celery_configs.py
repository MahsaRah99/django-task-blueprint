from celery import Celery
from datetime import timedelta
import os
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_interview.settings')

celery_app = Celery('backend_interview')
celery_app.autodiscover_tasks()

# Celery Configuration
celery_app.conf.broker_url = 'redis://localhost:6379/0'
celery_app.conf.result_backend = 'redis://localhost:6379/0'
celery_app.conf.task_serializer = 'json'
celery_app.conf.result_serializer = 'pickle'
celery_app.conf.accept_content = ['json', 'pickle']
celery_app.conf.result_expires = timedelta(days=2)
celery_app.conf.task_always_eager = False
celery_app.conf.worker_prefetch_multiplier = 4

# Celery Beat Configuration
celery_app.conf.beat_schedule = {
    'send-restock-sms': {
        'task': 'user_management.tasks.send_restock_sms',
        'schedule': crontab(hour=21, minute=0),
    },
}