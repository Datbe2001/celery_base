import time
from celery_app import celery


@celery.task
def handle_sum(x, y):
    time.sleep(10)
    print("xy")
    print(x + y)
    return x + y


@celery.task
def periodic_sum(x, y):
    handle_sum.delay(x, y)


@celery.task
def another_periodic_task(x, y):
    handle_sum.delay(x, y)
