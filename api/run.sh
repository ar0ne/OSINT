#!/bin/sh

alembic upgrade head
uvicorn osint.main:app --host 0.0.0.0 --port 8000 
