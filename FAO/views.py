from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image

posts = [
    {
        'author':'Ryan Byrne',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author':'Logan Rupert',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'FAO/homePage.html', context)

def about(request):
    output = "In Development"
    return HttpResponse(output)

def tech(request):
    output = "In Development"
    return HttpResponse(output)

def project(request):
    output = "In Development"
    return HttpResponse(output)

def contacts(request):
    output = "In Development"
    return HttpResponse(output)

def repo(request):
    try:
        with open('FAO/assets/logo/Thumnail.png', "rb") as f:
            return HttpResponse(f.read(), content_type="image/png")
    except IOError:
        red = Image.new('RGBA', (1, 1), (255,0,0,0))
        response = HttpResponse(content_type="image/png")
        red.save(response, "png")
        return response