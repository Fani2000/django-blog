from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post, Author, Tag




def index(request):
  latest_posts = Post.objects.all().order_by('date')[:3]
  return render(request, 'blog/index.html', {"posts":latest_posts})

def posts(request):
  sorted_posts = Post.objects.all().order_by('date')
  return render(request, "blog/all-posts.html", {"posts": sorted_posts})

def post(request, slug):
  post = get_object_or_404(Post, slug=slug) 
  # post = next(post for post in all_posts if post['slug'] == slug)

  return render(request, "blog/post-details.html", {"post": post, 'post_tags': post.tags.all()})