from django.shortcuts import render,redirect
from .models import Post,Comment
from .forms import Postform,CommentForm
from django.views.generic import ListView,DeleteView,CreateView

# all posts
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

    return render(request,'blog/edit_post.html',{'form':form })

#---------------------------------------------------
#delete 
#class based views
class Delete_post(DeleteView):
    model =Post
    success_url ='/blog/'
#---------------------------------------------------
