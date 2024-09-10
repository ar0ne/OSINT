
source .venv/bin/activate

cd src

celery -A app.tasks.celery worker --loglevel=info
