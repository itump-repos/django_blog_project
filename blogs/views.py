from django.db import models
from django.db.models.base import Model
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from .models import Post
from django.urls import reverse_lazy


class PostUpdateView(UpdateView):

    # update Posts!

    model = Post
    fields = ['title', 'slug', 'content', 'image']
    template_name_suffix = '_update_form'


class PostListView(ListView):

    # Read/Retrieve
    model = Post


class PostDetailView(DetailView):

    # Read/Retrieve

    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'slug', 'content', 'image']
    success_url = reverse_lazy('PostList')
