
from django.views.generic import ListView, DetailView

from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "aipost/list.html"
    # queryset = Post.objects




class PostDetailView(DetailView):
    model = Post
    template_name = "aipost/detail.html"