from django.db import models

# Create your models here.
class Product(models.Model):
    libelle=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    image=models.ImageField()
    categorie=models.CharField(max_length=50)


class Category(models.Model):
    libelle=models.ForeignKey(Product, on_delete=models.CASCADE)