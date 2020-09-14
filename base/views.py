from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'base/index.html')


def posts(request):
    posts=[
        {'headline':'calculator',
        'sub_headline':'this is a calculator app'},
        {'headline':'weather App',
        'sub_headline':'this is weather app to prodict weather changes'},
        {'headline':'todo list',
        'sub_headline':'this is the todo list to remember things'}
    ]
    context={'posts':posts}
    return render(request, 'base/posts.html')


def post(request):
    return render(request, 'base/post.html')


def profile(request):
    return render(request, 'base/profile.html')
