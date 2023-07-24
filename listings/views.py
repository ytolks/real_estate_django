from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.shortcuts import get_object_or_404
from listings.choices import price_choices,bedroom_choices,state_choices
# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request,listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing }
    return render(request, 'listings/listing.html',context)

def search(request):
    #get all listings from database
    query_set_list = Listing.objects.order_by('-list_date')
#keywords

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_set_list = query_set_list.filter(description__icontains=keywords,)

#city - starts with 

    if 'city' in request.GET:
        keywords = request.GET['city']
        if keywords:
            query_set_list = query_set_list.filter(city__istartswith=keywords)

#State
    if 'state' in request.GET:
        keywords = request.GET['state']
        if keywords:
            query_set_list = query_set_list.filter(state__iexact=keywords,)

#Bedrooms
    if 'bedrooms' in request.GET:
        keywords = request.GET['bedrooms']
        if keywords:
            query_set_list = query_set_list.filter(bedrooms__lte=keywords,)

#Price
    if 'price' in request.GET:
        keywords = request.GET['price']
        if keywords:
            query_set_list = query_set_list.filter(price__lte=keywords,)
    context  = {

        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'listings': query_set_list,
        'values':request.GET,

    }
    return render(request, 'listings/search.html',context)
