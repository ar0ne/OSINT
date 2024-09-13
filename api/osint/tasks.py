import os

from celery import Celery
from dotenv import load_dotenv

load_dotenv()


CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
CELERY_BACKEND_URL = os.environ.get("CELERY_BACKEND_URL")

celery = Celery(
    "osint",
    broker=CELERY_BROKER_URL,
    backend=CELERY_BACKEND_URL
)
celery.autodiscover_tasks(["osint.scans.tasks"])
