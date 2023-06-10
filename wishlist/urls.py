from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('wishlist/remove/<int:wishlist_id>/',
         views.wishlist_remove, name='wishlist_remove'),
]
