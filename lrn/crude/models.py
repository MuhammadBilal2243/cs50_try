from django.db import models

# Create your models here.
class tasks(models.Model):
    title=models.CharField(max_length=30)
    detail=models.CharField(max_length=300)
    post_time=models.TimeField(auto_now_add=True)

