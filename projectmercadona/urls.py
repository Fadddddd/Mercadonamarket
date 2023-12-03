"""
URL configuration for projectmercadona project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from merchandise.views import accueil, contact, aboutus, products, privacy, search_view, category, category_product_list
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accueil, name="accueil"),
    path('contact/', contact, name='contact'),
    path('aboutus/', aboutus, name='aboutus'),
    path('products/', products, name='products'),
    # path('categories/', categories, name='categories'),
    path('privacy/', privacy, name='privacy'),
    path('merchandise/', include("merchandise.urls")),
    path('search/', search_view, name="search"),
    path('category/', category, name="category"),
    path('category/<id>/', category_product_list, name="category_product_list"),
    path('admin-button/', views.admin_button, name='admin_button'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


