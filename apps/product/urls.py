from django.urls import path
from .views import *

app_name = 'product'
urlpatterns = [
    path('', home, name='home'),

    path('product/', product, name='product'),
    path('product-details/<int:product_id>', product_details, name='product_details'),
    path('shopping-cart/', shoping_cart, name='shopping_cart'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

]
