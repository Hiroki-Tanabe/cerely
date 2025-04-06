from django.db import models
from django.utils.timezone import now

# Create your models here.

class MyModel(models.Model):
    column1 = models.CharField(max_length=255, default="default_value")
    column2 = models.IntegerField(default=0)  # デフォルト値を設定
    column3 = models.DateTimeField(default=now)