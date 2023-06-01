from django.db import models
from products.models import Product

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    rating_value = models.IntegerField()

    def __str__(self):
        return f"{self.rating_value} - {self.product}"
