from django.shortcuts import render

from merchandise.models import Category, Product

def accueil(request):
    products=Product.objects.filter()[0:6]
    categories=Category.objects.all()
    return render (request, 'merchandise/index.html',
    {'products':products,'categories':categories})

# def contact(request):
#     return render (request, 'merchandise/contact.html')

def aboutus(request):
    return render(request, 'merchandise/aboutus.html')

def products(request):
    products=Product.objects.all()
    return render(request, 'merchandise/products.html',
    {'products':products})

# def product_detail(request, id):
#     product=Product.objects.get(id=id)
#     return render(request, 'merchandise/product_detail.html',
#                   {'product':product})

# def category_detail(request, id):
#     category=Category.objects.get(id=id)
#     products=Product.objects.filter(category=category)
#     return render(request, 'merchandise/category_detail.html',
#                   {'category':category, 'products':products})

def search_view(request):
    query = request.GET.get('q')
    products = Product.objects.filter(
        libelle__icontains=query)
    context={
        "products" : products,
        "query": query,
    }
    return render(request, "merchandise/search.html", context)

def category(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    context= {
        "categories": categories,
        "products": products,
    }
    return render (request, 'merchandise/category.html',
    context)

def category_product_list(request, id):
    category=Category.objects.get(id=id)
    products=Product.objects.filter(category=category)

    context= {
        "category": category,
        "products": products
    }
    return render (request, "merchandise/category_product_list.html", context)


def privacy(request):
    return render(request, 'merchandise/privacy.html')

