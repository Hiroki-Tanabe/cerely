from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from .models import MyModel  # データベースモデルをインポート


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