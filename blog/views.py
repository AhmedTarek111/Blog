from django.shortcuts import render,redirect
from .models import Post
from .forms import Postform
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView

# all posts
# function 
def post_list(request):
    data= Post.objects.all()
    return render(request,'post_list.html',{'Posts':data})

#class based views
class Post_list(ListView):
    model=Post
    context_object_name ='all_posts'

#---------------------------------------------------
# post details 
#   function
def all_post_details(request,post_id):
    data= Post.objects.get(id=post_id)
    return render (request,'post_details.html',{'post_details':data})

#   class based views 
class Post_detalis(DetailView):
    model = Post
    template_name ="blog/post_details.html"
    context_object_name ='post_details'
#---------------------------------------------------

#add post
# function 
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

#class based views
class AddPost(CreateView):
    model = Post
    template_name ="blog/add_newpost.html"
    fields='__all__'
    success_url ='/blog/'
#---------------------------------------------------

#edit post
#function 
def edit_post(request,post_id):
    data= Post.objects.get(id=post_id)
    if request.method == 'POST':
        form=Postform(request.POST,request.FILES, instance=data)
        if form.is_valid():
            form.save()
    else:
        form=Postform(instance=data)
    return render(request,'edit_post.html',{'form':form})
#class based views
class EditPost(UpdateView):
    model =Post
    template_name ='blog/edit_post.html'
    fields =['title','content','create_date','draft','tags','image','author']
    success_url ='/blog/'
#---------------------------------------------------
#delete 
#function 

def delete_post(request,post_id):
        delete= Post.objects.get(id=post_id).delete()
        return render(request,'delete_post.html',{'delete':delete})

#class based views
class Delete_post(DeleteView):
    model =Post
    success_url ='/blog/'
#---------------------------------------------------
