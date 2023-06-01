# pylint: disable=no-member
from django.shortcuts import get_object_or_404, redirect
from .models import Rating
from products.models import Product 

def rate_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    rating_value = int(request.POST.get('rating'))
    Rating.objects.create(product=product, rating_value=rating_value)
    return redirect('product_detail', product_id=product_id)