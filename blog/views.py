from django.shortcuts import render
from .models import Post

def post_list(request):
    data= Post.objects.all()
    return render(request,'post_list.html',{'Posts':data})

def all_post_details(request,value):
    data= Post.objects.get(id=value)
    return render (request,'post_details.html',{'post_details':data})