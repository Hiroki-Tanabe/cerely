# ベースイメージ
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y
COPY ./beat/requirements.txt ./
RUN pip install -r requirements.txt

COPY ../tasks.py ./tasks.py
COPY ../celery_config.py ./celery_config.py
CMD ["celery", "-A", "tasks", "beat", "--loglevel=info"]
# CMD ["sh", "-c", "while true; do sleep 3600; done"]
