# pylint: disable=no-member
from wishlist.models import WishlistItem
from products.models import Product
from rating.models import Rating
from django.db.models import Avg

def wishlist_count(request):
    count = 0
    if request.user.is_authenticated:
        count = WishlistItem.objects.filter(user=request.user).count()
    return {'wishlist_count': count}

def average_rating(request):
    products = Product.objects.all()

    for product in products:
        rating = Rating.objects.filter(product=product).aggregate(Avg('rating_value'))
        product.rating = rating['rating_value__avg']

    return {'products': products}    