from celery import Celery

# Tạo instance của Celery
celery = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

celery.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    beat_schedule={
        'periodic_sum-task': {
            'task': 'tasks.periodic_sum',
            'schedule': 5.0,
            'args': (1, 1)
        },
        'periodic-sum-another-task': {
            'task': 'tasks.another_periodic_task',
            'schedule': 10.0,
            'args': (2, 3)
        }
    }
)

import tasks
