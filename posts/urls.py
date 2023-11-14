from django.urls import path
# from .views import post_list, post_detail
from .views import PostList, PostDetail
urlpatterns = [
    # path('posts/', post_list , name='post-list'),
    path('posts/', PostList.as_view() , name='post-list'),
    path('post/<int:pk>/', PostDetail.as_view() , name='post-detail'),
    # path('post/<int:post_id>/', post_detail , name='post-detail'),
    
    
    
]
