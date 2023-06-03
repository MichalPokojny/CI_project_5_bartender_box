from django.contrib import admin
from .models import Product, Category, Review

# Register the Product model with the admin site
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

# Register the Review model with the admin site
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'comment',
        'created_at'
    )

# Register the Category model with the admin site
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )