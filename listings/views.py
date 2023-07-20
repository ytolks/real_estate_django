from django.shortcuts import render

# Create your views here.

def index(request, *args, **kwargs):
    return render(request, 'listings/listings.html',)

def listing(request, *args, **kwargs):
    return render(request, 'listings/listings.html',)

def search(request, *args, **kwargs):
    return render(request, 'listings/listings.html',)
