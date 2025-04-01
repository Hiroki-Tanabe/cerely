#!/bin/bash

# migrateコマンドを実行

python watchProject/manage.py makemigrations
python watchProject/manage.py migrate

# サーバーを起動
python watchProject/manage.py runserver 0.0.0.0:8000