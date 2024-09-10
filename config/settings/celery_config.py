from celery.schedules import crontab


CELERY_BROKER_URL = 'redis://aksiya_mix_redis:6379/0'

CELERY_RESULT_BACKEND = 'redis://aksiya_mix_redis:6379/1'

CELERY_TIMEZONE = "Asia/Tashkent"

CELERY_TASK_TRACK_STARTED = True
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True


CELERY_BEAT_SCHEDULE = {
    'run-task-every-midnight': {
        'task': 'apps.general.tasks.get_currency',
        'schedule': crontab(hour=0, minute=0),
    },
}