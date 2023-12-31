from django.urls import path
from .views import post_list, post_detail, create_post, edit_post, delete_post
# from .views2 import PostList, PostDetail, CreatePost, EditPost, DeletePost
from .api import post_list_api, post_detail_api, PostListAPI, PostDetailAPI, PostAPI



urlpatterns = [
    path('posts/', post_list , name='post-list'),
    path('post/<int:pk>/', post_detail , name='post-detail'),
    path('post/create/', create_post , name='create-post'),
    path('post/<int:pk>/update/', edit_post , name='update-post'),
    path('post/<int:pk>/delete/', delete_post , name='delete-post'),
    path('posts/api/', PostListAPI.as_view() , name="post-list-api"),
    path('post/api/<int:pk>', PostDetailAPI.as_view() , name="post-detail-api"),
    path('all/posts/api/<int:pk>', PostAPI.as_view() , name="post-api"),
    
    # path('posts/', PostList.as_view() , name='post-list'),
    # path('post/<int:pk>/', PostDetail.as_view() , name='post-detail'),
    # path('post/create/', CreatePost.as_view() , name='create-post'),
    # path('post/<int:pk>/update/', EditPost.as_view() , name='update-post'),
    # path('post/<int:pk>/delete/', DeletePost.as_view() , name='delete-post'),
    
    
    
    
    
    
]
