# pylint: disable=no-member
from wishlist.models import WishlistItem
from products.models import Product
from rating.models import Rating
from django.db.models import Avg


def wishlist_count(request):
    """
    Retrieves the count of wishlist items for the authenticated user.
    """
    count = 0

    if request.user.is_authenticated:
        # If authenticated, count the number of wishlist items for the user
        count = WishlistItem.objects.filter(user=request.user).count()

    # Return a dictionary with the 'wishlist_count' key and the count value
    return {'wishlist_count': count}


def average_rating(request):
    """
    Calculates the average rating value for each product.
    """
    products = Product.objects.all()

    for product in products:
        # Retrieve the average rating value for the
        #  product using the Rating model and the `aggregate` function
        rating = Rating.objects.filter(
            product=product).aggregate(Avg('rating_value'))

        # Assign the average rating value to the product's `rating` attribute
        product.rating = rating['rating_value__avg']

    return {'products': products}
