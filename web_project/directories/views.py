from django.http import HttpResponse

def index(request):
    output = "hi"
    return HttpResponse(output)