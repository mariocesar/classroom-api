from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/docs/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = [
        path("__debug__", include("debug_toolbar.toolbar")),
        *urlpatterns
    ]
