# pylint: disable=no-member
from django.shortcuts import render
from .models import WishlistItem

def wishlist(request):
    """View for displaying the user's wishlist"""
    
    # Retrieve the wishlist items for the current user
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})
