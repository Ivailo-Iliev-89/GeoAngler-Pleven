from .models import Post
from django.views.generic import ListView, DetailView


class PostListView(ListView):

    model = Post
    template_name = 'blog/post_index.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):

    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
