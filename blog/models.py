from django.db import models
from django.utils import timezone


class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=40000)
    create_date=models.DateTimeField(default=timezone.now())
    draft=models.BooleanField(default=True)