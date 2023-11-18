from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm
# CRUD using FBV

def post_list(request):
    posts = Post.objects.all()                               # :query
    context = {'posts' : posts}                              # :context
    return render(request, 'posts/post_list.html', context)  # : Template

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post':post}
    return render(request, 'posts/post_detail.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
        return redirect('/posts/')
        
    else:
        form = PostForm()
        
    return render(request, 'posts/post_form.html', {'form':form})
    

def edit_post(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
        return redirect('/posts/')
    
    else:
        form = PostForm(instance=post)
        
    return render(request, 'posts/edit.html', {'form':form}) 


def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/posts/') 
         
        


# CRUD using CBV
class PostList(ListView):
    model = Post
    
class PostDetail(DetailView):
    model = Post
    
class CreatePost(CreateView):
    model = Post
    fields = '__all__'                        # will lookup for (post_form.html)
    success_url = '/posts/'


class EditPost(UpdateView):
    model = Post
    fields = '__all__'
    success_url = '/posts/'
    template_name = 'posts/edit.html'
    
    
class DeletePost(DeleteView):
    model = Post
    success_url = '/posts/'
    

