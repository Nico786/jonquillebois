from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('786-pgm-admin-page/', admin.site.urls),
    path('', include('app.urls') )
]
