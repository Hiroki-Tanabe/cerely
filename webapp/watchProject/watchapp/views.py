from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from .models import MyModel  # データベースモデルをインポート
from django.db import connection  # Djangoのデータベース接続を使用


# from ...celery.tasks import sample_task  # Celeryタスクをインポート

# def run_task(request):
#     if request.method == "POST":
#         sample_task.delay("ボタンからの実行！")
#         return HttpResponse("タスクが実行されました！")
    # return render(request, 'template.html')

def say_hello(request):
    message = ""
    if request.method == "POST":
        message = "ハロー！"
    return render(request, 'template.html', {'message': message})

def add_and_display(request):
    if request.method == "POST":
        # フォームの入力値を取得し、データベースに追加
        new_data = request.POST.get('new_data')
        if not new_data:  # データが空の場合
            return JsonResponse({'error': 'データが空です。値を入力してください！'})
        MyModel.objects.create(field_name=new_data)
    # データベースの全データを取得
    all_data = list(MyModel.objects.values())
    return JsonResponse({'data': all_data})  # JSON形式でフロントエンドに送信

def fetch_table_data(request):
    if request.method == "POST":
        # テーブルデータを直接取得
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM watchapp_mymodel")
            rows = cursor.fetchall()

        # データを返す（JSON形式でも可能）
        return JsonResponse({'data': rows})
    return render(request, 'fetch_data.html')

def add_data(request):
    if request.method == "POST":
        # データを保存
        new_name = request.POST.get('name', 'デフォルト名')  # POSTリクエストからデータ取得
        obj = MyModel.objects.create(name=new_name)
        obj.save()
        return JsonResponse({"message": f"データ '{new_name}' を保存しました！"})
    return render(request, 'add_data.html')