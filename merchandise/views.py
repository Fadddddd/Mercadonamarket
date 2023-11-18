from django.shortcuts import render

def accueil(request):
    return render (request, 'merchandise/header.html')

def contact(request):
    return render (request, 'merchandise/contact.html')

def aboutus(request):
    return render(request, 'merchandise/aboutus.html')