from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

posts =  [
    {
        'author' : 'Tony',
        'title' : 'Blog post 1',
        'content' : 'I am Iron Man',
        'date_posted': 'August 26, 2024'
    },
    {
        'author' : 'Tony',
        'title' : 'Blog post 1',
        'content' : 'I am Iron Man',
        'date_posted': 'August 26, 2024'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'landing/home.html', context)

def about(request):
    return render(request, 'landing/about.html', {'title': 'About'})