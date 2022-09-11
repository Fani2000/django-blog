from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls  import reverse
from .forms import CommentForm
from .models import Post
from django.views import View
from django.views.generic import ListView, DetailView

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


class PostView(View):
  template_name = 'blog/post-details.html'
  model = Post
  context_object_name = "post"

  def get(self,request, slug):
    post = Post.objects.get(slug=slug)
    context = {
      'post': post,
      "post_tags": post.tags.all(),
      "comment_form": CommentForm(),
      "comments": post.comments.all().order_by('-id')
    }
    return render(request, 'blog/post-details.html', context)

  def post(self, request, slug):
    comment_form = CommentForm(request.POST)
    post = Post.objects.get(slug=slug)

    if comment_form.is_valid():
      comment = comment_form.save(commit=False) 
      comment.post = post
      comment.save()
      return HttpResponseRedirect(reverse("post-details", args=[slug]))

    context = {
      'post': post,
      "post_tags": post.tags.all(),
      "comment_form": CommentForm(),
      "comments": post.comments.all().order_by('-id')
    }
    return render(request, 'blog/post-details.html', context)

  # def get_context_data(self, **kwargs):
  #     context = super().get_context_data(**kwargs)
  #     context['comment_form'] = CommentForm()
  #     context['post_tags'] = self.object.tags.all()
  #     return context
  
