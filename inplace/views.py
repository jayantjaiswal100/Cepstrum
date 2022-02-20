from django.shortcuts import render
from .models import Post
# Create your views here.
from django.views.generic import ListView, DetailView



class InplaceListView(ListView):
    model = Post
    template_name = "inplace/inplace_list.html"
    ordering = ['-created_at']


class PostDetailView(DetailView):
    model = Post
    template_name = "inplace/inplace_detail.html"


