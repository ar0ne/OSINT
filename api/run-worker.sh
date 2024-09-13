#!/bin/sh

celery -A osint.tasks.celery worker --loglevel=info
