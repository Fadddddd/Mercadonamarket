from django.shortcuts import render

def accueil(request):
    return render (request, 'merchandise/header.html')