from django.shortcuts import render
from django.http import HttpRequest
# from datetime import datetime


# Create your views here.

def index(request: HttpRequest) -> HttpRequest:
    # return HttpResponse("<h1>Hello world. You're at the polls index.</h1>")
    return render(request, 'index.html')
