from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.

def index(request, *args, **kwargs):
    listings = Listing.objects.all()
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, *args, **kwargs):
    return render(request, 'listings/listing.html',)

def search(request, *args, **kwargs):
    return render(request, 'listings/search.html',)
