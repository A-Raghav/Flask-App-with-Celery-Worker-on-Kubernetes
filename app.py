from celery import Celery
import time

celery_app = Celery(
    "app",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1"
)

@celery_app.task(name="Add 2 numbers")
def addition(i, j):
    time.sleep(2)
    return i + j

def func():
    for i in range(12):
        print(addition.delay(i, i))
    
if __name__=="__main__":
    func()