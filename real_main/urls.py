
from django.contrib import admin
from django.urls import path, include
# add modules for the media files shown in the web page
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('listings/',include('listings.urls')), # including pages app urls
    path('accounts/',include('accounts.urls')),
    path('contacts/',include('contacts.urls')),
     # including pages app urls
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 