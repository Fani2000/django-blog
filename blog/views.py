from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Main index page')

def posts(request):
    return HttpResponse('Posts')

def post(request, slug):
    return HttpResponse(f"Post {slug}")