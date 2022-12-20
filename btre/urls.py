from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('contacts/', include('contacts.urls')),
    path('listings/', include('listings.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# admin.site.site_header  =  "Custom bookstore admin"  
# admin.site.site_title  =  "BT Real Estate Admin"
admin.site.index_title  =  "BT Real Estate Admin"