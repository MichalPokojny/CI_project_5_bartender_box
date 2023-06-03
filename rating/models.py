from django.db import models
from products.models import Product
from django.contrib.auth.models import User

class Rating(models.Model):
    """ Rating model """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    value = models.IntegerField()  

    def __str__(self):
        return f"{self.value} - {self.product}"

    class Meta:
        unique_together = ('user', 'product')    
