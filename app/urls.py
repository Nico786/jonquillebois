from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('agencement', views.arrangement, name="arrangement"),
    path('mobilier', views.furnitures, name="furnitures"),
    path('contact', views.contact, name="contact"),
]