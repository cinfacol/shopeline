import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("supersecret/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("api/products/", include("apps.products.urls")),
    path("api/profile/", include("apps.profiles.urls")),
    path("api/ratings/", include("apps.ratings.urls")),
    path("api/enquiries/", include("apps.enquiries.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Shopeline Admin"
admin.site.site_title = "Shopeline Admin Portal"
admin.site.index_title = "Welcome to Shopeline Admin Portal"
