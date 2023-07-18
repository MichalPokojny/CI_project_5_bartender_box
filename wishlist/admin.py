from django.contrib import admin
from .models import WishlistItem


class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'added_at']
    list_filter = ['user', 'added_at']
    search_fields = ['user__username', 'product__name']

admin.site.register(WishlistItem, WishlistItemAdmin)
