from django.shortcuts import render

def home(request):
  return render(request, 'home.html')

def arrangement(request):
  return render(request, 'arrangement.html')

def furnitures(request):
  return render(request, 'furnitures.html')

def contact(request):
  return render(request, 'contact.html')