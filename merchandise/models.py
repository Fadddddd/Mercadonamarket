from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    libelle=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.category

    class Meta:
        verbose_name_plural="Categories"

class Product(models.Model):
    libelle=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    image=models.ImageField(upload_to='merchandise_images', blank=True, null=True)
    libelle_category=models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    author=models.ForeignKey(User, related_name="Products", on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Products"

    def __str__(self):
        return self.libelle


