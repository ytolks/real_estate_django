from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request, *args, **kwargs):
    return HttpResponse('<h1>Real Estate home page</h1>')
