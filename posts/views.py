from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
# CRUD using FBV

# def post_list(request):
#     posts = Post.objects.all()                               # :query
#     context = {'posts' : posts}                              # :context
#     return render(request, 'posts/post_list.html', context)  # : Template

# def post_detail(request, post_id):
#     post = Post.objects.get(id=post_id)
#     context = {'post':post}
#     return render(request, 'posts/post_detail.html', context)






# CRUD using CBV
class PostList(ListView):
    model = Post
    
class PostDetail(DetailView):
    model = Post
    



