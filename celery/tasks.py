from celery import Celery
import datetime

# Celeryインスタンスを作成
app = Celery('tasks')
app.config_from_object('celery_config')  # 設定を読み込む

# タスクを定義
@app.task
def sample_task():
    print(f"タスク実行: {datetime.datetime.now()}")
    return "Task Completed"


# from django.conf import settings
# import django
# django.setup()

# from watchapp.models import MyModel  # Djangoモデル

# @app.task
# def update_database_task(data):
#     obj = MyModel.objects.create(field_name=data)
#     return f"Database updated with: {obj}"