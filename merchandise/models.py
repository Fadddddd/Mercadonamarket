from django.db import models
from cloudinary.models import CloudinaryField



class Category(models.Model):
    libelle = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.libelle

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    libelle = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = CloudinaryField('image', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")

    def __str__(self):
        return self.libelle

class Promotion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=0)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Promotions"

    @property
    def get_discounted_price(self):
        if self.discount_percentage > 0:
            price_now = self.product.price - (self.product.price * self.discount_percentage / 100)
        else:
            price_now = self.product.price

        return price_now

    def __str__(self):
        return f"{self.discount_percentage}% off until {self.end_date}"
