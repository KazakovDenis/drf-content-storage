import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'content_storage.core.settings')

app = Celery('content_storage')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
