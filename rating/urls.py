from django.urls import path
from .import views


urlpatterns = [
    path('rate_product/<int:product_id>/', views.rate_product, name='rate_product'),
]