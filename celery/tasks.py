from celery import Celery
import datetime
import requests
from ..webapp.models import MyModel

# Celeryインスタンスを作成
app = Celery('tasks')
app.config_from_object('celery_config')  # 設定を読み込む

# タスクを定義
@app.task
def sample_task():
    print(f"タスク実行: {datetime.datetime.now()}")
    return "Task Completed"

    # """
    # Celeryタスク: データを指定されたエンドポイントに送信
    # """
    # url = 'http://localhost/add-and-display/'  # エンドポイントURL
    # headers = {
    #     'Content-Type': 'application/json',
    #     'X-CSRFToken': 'your_csrf_token_here'  # 必要に応じてCSRFトークンを設定
    # }
    # data = "hello"

    # try:
    #     response = requests.post(url, json={'new_data': data}, headers=headers)
    #     response.raise_for_status()  # HTTPエラーをチェック
    #     return f"データ送信成功: {response.json()}"
    # except requests.exceptions.RequestException as e:
    #     return f"エラー発生: {str(e)}"