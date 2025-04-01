from django.db import models

# Create your models here.

class MyModel(models.Model):
    field_name = models.CharField(max_length=100)  # 追加するフィールド