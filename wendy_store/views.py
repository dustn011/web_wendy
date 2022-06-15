from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Post
# Create your views here.


class PostList(ListView):
    model = Post
    template_name = "wendy_store/post_detail_list.html"
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post
