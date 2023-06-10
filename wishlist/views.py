# pylint: disable=no-member
from django.shortcuts import render, redirect, get_object_or_404
from .models import WishlistItem


def wishlist(request):
    """View for displaying the user's wishlist"""

    # Retrieve the wishlist items for the current user
    wishlist_items = WishlistItem.objects.filter(user=request.user)

    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})


def wishlist_remove(request, wishlist_id):
    wishlist_item = get_object_or_404(WishlistItem, id=wishlist_id)
    wishlist_item.delete_from_wishlist()
    return redirect('wishlist')
