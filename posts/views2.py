from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



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
    