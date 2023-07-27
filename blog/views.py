from django.shortcuts import render,redirect
from .models import Post,Comment
from .forms import Postform,CommentForm
from django.views.generic import ListView,DeleteView,CreateView,UpdateView

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
def Post_detalis(request,pk):
    data = Post.objects.get(id=pk)
    comments = Comment.objects.all()
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user = request.user
            myform.post = data
            myform.save()
    else:
        form = CommentForm()
    return render(request,'blog/post_details.html', {"post_details":data , "comments":comments , "comment_form":form})


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
def edit_post(request,pk):
    data= Post.objects.get(id=pk)
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

def delete_post(request,pk):
        delete= Post.objects.get(id=pk).delete()
        return render(request,'delete_post.html',{'delete':delete})

#class based views
class Delete_post(DeleteView):
    model =Post
    success_url ='/blog/'
#---------------------------------------------------
