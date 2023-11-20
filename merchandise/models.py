from django.db import models

# Create your models here.

class Category(models.Model):
    libelle=models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.libelle

    class Meta:
        verbose_name_plural="Categories"

class Product(models.Model):
    libelle=models.CharField(max_length=100, blank=True, null=True)    
    description=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    image=models.ImageField(upload_to='merchandise_images', blank=True, null=True)
    categorie=models.ManyToManyField(Category)

    def __str__(self):
        return self.libelle


