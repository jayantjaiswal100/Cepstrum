from django.shortcuts import render
from .models import Post
# Create your views here.
from django.views.generic import ListView, DetailView
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from .serializers import PostSerializers
# Create your views here.



class InplaceListView(ListView):
    model = Post
    template_name = "inplace/inplace_list.html"
    ordering = ['-created_at']


class InplaceDetailView(DetailView):
    model = Post
    template_name = "inplace/inplace_detail.html"


class PostManList(mixins.ListModelMixin, GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class PostRetrive(mixins.RetrieveModelMixin, GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)


