from django.db import models
from django.utils import timezone 
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=40000)
    create_date=models.DateTimeField(default=timezone.now)
    draft=models.BooleanField(default=True)
    tags=TaggableManager()
    image=models.ImageField(upload_to='images')
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True, related_name='Post_User')
    def __str__(self):
        return self.title