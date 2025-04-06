from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from .models import MyModel  # データベースモデルをインポート
from django.db import connection  # Djangoのデータベース接続を使用
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
import json


def say_hello(request):
    message = ""
    if request.method == "POST":
        message = "ハロー！"
    return render(request, 'template.html', {'message': message})

def display_add_table_data(request):
    return render(request, 'add_table_data.html')

def display_fetch_table_data(request):
    print(f"{request.method}_display")
    return render(request, 'fetch_table_data.html')

@csrf_exempt
def api_fetch_table_data(request):
    print(f"{request.method}_api")
    if request.method == 'POST':
        data = list(MyModel.objects.values('column1', 'column2', 'column3'))
        return JsonResponse({"data": data}, status=200)
    return JsonResponse({"error": "無効なリクエストメソッド"}, status=405)

@csrf_exempt
def api_add_table_data(request):
    if request.method == 'POST':
        print(f"{request.body}")
        try:
            # JSONデータのパース
            body = json.loads(request.body)
            column1 = body.get('column1',"NULL")
            column2 = int(body.get('column2', 0))  
            column3 = body.get('column3', None)
            column3 = parse_datetime(column3)
            if column3 is None:
                return JsonResponse({"error": "無効な日時フォーマット"}, status=400)

            # 必須フィールドのチェック
            if not column1 or not column3:
                return JsonResponse({"error": "必須フィールドが不足しています"}, status=400)

            # モデルに保存（仮のモデル例：MyModel）
            new_entry = MyModel.objects.create(
                column1=str(column1),
                column2=int(column2),
                column3=column3
            )
            print("hello2")

            # 成功レスポンス
            return JsonResponse({
                "message": "データが追加されました",
                "data": {
                    "id": new_entry.id,
                    "column1": column1,
                    "column2": column2,
                    "column3": column3
                }
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "JSONデータの解析に失敗しました"}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"エラー: {str(e)}"}, status=400)

    return JsonResponse({"error": "無効なリクエストメソッドです"}, status=405)