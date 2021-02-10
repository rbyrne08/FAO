from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'homePage.html')

def about(request):
    output = "In Development"
    return HttpResponse(output)

