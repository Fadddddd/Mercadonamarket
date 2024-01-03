from django.shortcuts import render
from merchandise.models import Category, Product

def prepare_product_data(product):
    return {
        'libelle': product.libelle,
        'price': product.price,
        'image_url': product.image.url,
        'promotions': [
            {
                'discount_percentage': promotion.discount_percentage,
                'discounted_price': promotion.get_discounted_price(),
            }
            for promotion in product.promotion_set.all()
        ],
        'description': product.description,
    }

def accueil(request):
    products = Product.objects.filter()[0:6]
    categories = Category.objects.all()

    # Prepare product data for each product
    products_data = [prepare_product_data(product) for product in products]

    context = {'products_data': products_data, 'categories': categories}
    return render(request, 'merchandise/index.html', context)

def aboutus(request):
    return render(request, 'merchandise/aboutus.html')

def products(request):
    products = Product.objects.all()

    # Prepare product data for each product
    products_data = [prepare_product_data(product) for product in products]

    return render(request, 'merchandise/products.html', {'products_data': products_data})

def search_view(request):
    query = request.GET.get('q')
    products = Product.objects.filter(libelle__icontains=query)

    # Prepare product data for each product
    products_data = [prepare_product_data(product) for product in products]

    context = {'products_data': products_data, 'query': query}
    return render(request, "merchandise/search.html", context)

def category(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    # Prepare product data for each product
    products_data = [prepare_product_data(product) for product in products]

    context = {"categories": categories, "products_data": products_data}
    return render(request, 'merchandise/category.html', context)

def category_product_list(request, id):
    category = Category.objects.get(id=id)
    products = Product.objects.filter(category=category)

    # Prepare product data for each product
    products_data = [prepare_product_data(product) for product in products]

    context = {"category": category, "products_data": products_data}
    return render(request, "merchandise/category_product_list.html", context)

def privacy(request):
    return render(request, 'merchandise/privacy.html')
