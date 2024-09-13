#!/bin/sh

cd osint
alembic upgrade head
cd ..
uvicorn osint.main:app --host 0.0.0.0 --port 8000 
