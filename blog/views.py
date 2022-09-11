from django.shortcuts import get_object_or_404
from .models import Post, Author, Tag
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView

class IndexView(ListView):
  template_name = "blog/index.html"
  model = Post
  context_object_name = 'posts'

  def get_queryset(self):
    query_set = super().get_queryset()
    data = query_set[:3]
    return data
  

class PostsView(ListView):
  template_name = "blog/all-posts.html"
  model = Post
  ordering = ["-date"]
  context_object_name = "posts"


class PostView(DetailView):
  template_name = 'blog/post-details.html'
  model = Post
  context_object_name = "post"

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['post_tags'] = self.object.tags.all()
      return context
  
