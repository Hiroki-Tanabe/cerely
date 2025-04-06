FROM python:3.12

WORKDIR /app

ENV PYTHONUNBUFFERED 1   # この環境変数に値を入れることでバッファを無効化する('1'じゃなくてもいい)

RUN apt-get update && apt-get install -y
RUN apt-get install iputils-ping -y
RUN apt-get install netcat-openbsd -y
RUN apt-get install default-mysql-client -y
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

ENV PYTHONPATH=/app/watchProject

COPY . .

RUN chmod +x ./entrypoint.sh

# エントリポイントを設定
COPY ./entrypoint.sh /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
# ENTRYPOINT ["/app/entrypoint.sh"]
# CMD ["python", "watchProject/manage.py", "makemigrate"]
# CMD ["python", "watchProject/manage.py", "migrate"]
# CMD ["python", "watchProject/manage.py", "runserver", "0.0.0.0:8000"]