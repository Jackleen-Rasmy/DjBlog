from rest_framework.decorators import api_view
from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework import generics

@api_view(['GET'])
def post_list_api(request):
    posts = Post.objects.all()
    data = PostSerializer(posts, many=True).data
    return Response(
        {'data': data}
    )
    
    
@api_view(['GET'])
def post_detail_api(request,id):
    post = Post.objects.get(id=id)
    data = PostSerializer(post).data
    return Response(
        {
            'data':data
        }
    )
    
    
# # CRUD > CBV
# class PostListAPI(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostListAPI(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

  
class PostDetailAPI(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer   
    
    
class PostAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer      
    
    
    