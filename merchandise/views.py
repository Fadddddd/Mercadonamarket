from django.shortcuts import render
from merchandise.models import Category, Product

# def prepare_product_data(product):
#     return {
#         'libelle': product.libelle,
#         'price': product.price,
#         'image_url': product.image.url,
#         'promotions': [
#             {
#                 'discount_percentage': promotion.discount_percentage,
#                 'discounted_price': promotion.get_discounted_price(),
#             }
#             for promotion in product.promotion_set.all()
#         ],
#         'description': product.description,
#     }

#pb d'affichage des produits ici
def accueil(request):
    products=Product.objects.filter()[0:6]
    categories=Category.objects.all()
    context= {
        "categories": categories,
        "products": products,
    }
    return render (request, 'merchandise/index.html',
    {'products':products,'categories':categories})

def aboutus(request):
    return render(request, 'merchandise/aboutus.html')

#probleme d'affichage des prod ici aussi
def products(request):
    products=Product.objects.all()
    return render(request, 'merchandise/products.html',
    {'products':products})

#images fonctionnent pas
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

#ca aussi ca fonctionne pas pr le display d'images
def category_product_list(request, id):
    category=Category.objects.get(id=id)
    products=Product.objects.filter(category=category)

    context= {
        "category": category,
        "products": products,
    }
    return render (request, "merchandise/category_product_list.html", context)



def privacy(request):
    return render(request, 'merchandise/privacy.html')
