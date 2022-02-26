from rest_framework import generics,permissions
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset= Post.objects.all()
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset= Post.objects.all()
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer