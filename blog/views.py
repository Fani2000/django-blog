from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView

# def index(request):
#   latest_posts = Post.objects.all().order_by('date')[:3]
#   return render(request, 'blog/index.html', {"posts":latest_posts})

class IndexView(TemplateView):
  template_name = "blog/index.html"
  model = Post

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['posts'] = self.model.objects.all().order_by('date')[:3]
    return context

class PostsView(ListView):
  template_name = "blog/all-posts.html"
  model = Post
  context_object_name = "posts"

# def posts(request):
#   sorted_posts = Post.objects.all().order_by('date')
#   return render(request, "blog/all-posts.html", {"posts": sorted_posts})

class PostView(DetailView):
  template_name = 'blog/post-details.html'
  model = Post
  context_object_name = "post"

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      post_object = get_object_or_404(self.model, slug=self.kwargs['slug'])
      context['post_tags'] = post_object.tags.all()
      return context
  

# def post(request, slug):
#   post = get_object_or_404(Post, slug=slug) 
#   # post = next(post for post in all_posts if post['slug'] == slug)

#   return render(request, "blog/post-details.html", {"post": post, 'post_tags': post.tags.all()})