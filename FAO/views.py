from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image

def home(request):
    return render(request, 'FAO/homePage.html')

def about(request):
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