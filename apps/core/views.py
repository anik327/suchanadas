# from core.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, BlogSettings


class HomeView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    site = BlogSettings
    template_name = 'home.html'
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'
