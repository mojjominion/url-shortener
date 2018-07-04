from .base import *


SECURE_SSL_REDIRECT = False

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
BROKER_POOL_LIMIT = 3

from celery.schedules import crontab

# Other Celery settings
CELERY_BEAT_SCHEDULE = {
    'auto-expire': {
        'task': 'shortner.tasks.auto_expire',
        'schedule': crontab(minute=10),
        # 'args': (*args)
    },
}