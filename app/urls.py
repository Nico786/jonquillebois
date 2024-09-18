from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('agencement', views.arrangements, name="arrangements"),
    path('arrangement/<int:pk>/', views.arrangement_detail, name='arrangement_detail'),
    path('mobilier', views.furnitures, name="furnitures"),
    path('contact', views.contact, name="contact"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)