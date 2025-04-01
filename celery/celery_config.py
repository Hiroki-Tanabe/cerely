import os
from celery.schedules import crontab

# broker_url = 'redis://redis:6379/0'
broker_url = os.environ['CELERY_BROKER_URL']
result_backend = broker_url

beat_schedule = {
    'sample-task-every-minute': {
        'task': 'tasks.sample_task',
        'schedule': crontab(minute='*'),  # 毎分実行
    },
}

# タイムゾーン設定
timezone = 'Asia/Tokyo'
enable_utc = True
