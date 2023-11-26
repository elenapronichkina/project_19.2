from django.shortcuts import render
from django.views.generic import CreateView

from blog.models import Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'body')