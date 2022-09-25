from celery import Celery
import time
import os


CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL", "NA")
CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND", "NA")

celery_app = Celery(
    "tasks",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)

@celery_app.task(name="Square the Number")
def square(i):
    time.sleep(2)
    return i**2