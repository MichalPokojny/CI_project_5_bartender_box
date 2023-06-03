# pylint: disable=no-member
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Rating
from products.models import Product 

@login_required
def rate_product(request, product_id):
    """Rate a product"""
    
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        rating_value = request.POST.get('rating')

        # Check if the user has already rated the product
        rating = Rating.objects.filter(user=request.user, product=product).first()
        if rating:
            rating.value = rating_value
            rating.save()
        else:
            rating = Rating.objects.create(user=request.user, product=product, value=rating_value)

        # Redirect to the product detail page or display a success message
        return redirect('product_detail', product_id=product.id)

    # Handle GET request or render a template for rating submission
    return render(request, 'rate_product.html', {'product': product})