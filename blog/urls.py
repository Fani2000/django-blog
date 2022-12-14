from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="starting-page"),
    path("posts", views.PostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.PostView.as_view(), name="post-details")
]
