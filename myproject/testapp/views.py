from django.shortcuts import render
from rest_framework import generics
from . models import BlogPost
from . serializers import BlogSerializer

# Create your views here.

class listcreateserializer(generics.ListCreateAPIView):
    queryset= BlogPost.objects.all()
    serializer_class=BlogSerializer

class RetrieveBlogView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer

class ListBlogView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer

class DeleteViewBlog(generics.DestroyAPIView):
    queryset=BlogPost.objects.all()
    serializer_class=BlogSerializer
    lookup_field='pk'