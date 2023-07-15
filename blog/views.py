from django.shortcuts import render,redirect
from .models import Post
from .forms import Postform
def post_list(request):
    data= Post.objects.all()
    return render(request,'post_list.html',{'Posts':data})

def all_post_details(request,post_id):
    data= Post.objects.get(id=post_id)
    return render (request,'post_details.html',{'post_details':data})

def add_new_post(request):
    if request.method == 'POST':
        form=Postform(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=False)        
            author=request.user
            form.save()        
            return redirect('/blog')
    else:
        form=Postform()
    return render(request,'add_newpost.html',{'form':form})

def edit_post(request,post_id):
    data= Post.objects.get(id=post_id)
    if request.method == 'POST':
        form=Postform(request.POST,request.FILES, instance=data)
        if form.is_valid():
            form.save()
    else:
        form=Postform(instance=data)
    return render(request,'edit_post.html',{'form':form})
    
def delete_post(request,post_id):
        delete= Post.objects.get(id=post_id).delete()
        return render(request,'delete_post.html',{'delete':delete})

