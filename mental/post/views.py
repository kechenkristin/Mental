from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .form import PostForm
from .models import Post


# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = "post/post_list.html"


def post_list(request):
    post = Post.objects.all()
    return render(request, 'post/post_list.html', {'post_list': post})



class CreatePostView(CreateView):  # new
    model = Post
    form_class = PostForm
    template_name = "post/add_post.html"
    success_url = reverse_lazy("post_list")