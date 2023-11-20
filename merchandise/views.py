from django.shortcuts import render

from merchandise.models import Category, Product

def accueil(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    return render (request, 'merchandise/index.html',
    {'products':products,'categories':categories})

def contact(request):
    return render (request, 'merchandise/contact.html')

def aboutus(request):
    return render(request, 'merchandise/aboutus.html')