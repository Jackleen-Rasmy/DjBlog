from django.shortcuts import render, redirect
from .models import *
from .forms import PostForm, CommentForm
# CRUD using FBV

def post_list(request):
    posts = Post.objects.all()                               # :query
    context = {'post_list' : posts}                              # :context
    return render(request, 'posts/post_list.html', context)  # : Template

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comments.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.post = post
            myform.save()
            
    else:
        form = CommentForm()
    
    context = {
        'post':post,
        'comments':comments,
        'form':form,
        }
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
         
        



