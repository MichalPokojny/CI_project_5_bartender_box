from wishlist.models import WishlistItem


def wishlist_count(request):
    count = 0
    if request.user.is_authenticated:
        count = WishlistItem.objects.filter(user=request.user).count()
    return {'wishlist_count': count}