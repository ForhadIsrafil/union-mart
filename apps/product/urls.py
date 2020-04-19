from django.urls import path
from .views import *

app_name = 'product'
urlpatterns = [
    path('', home, name='home'),

    path('products/', product, name='product'),
    path('product-details/<int:product_id>/', product_details, name='product_details'),
    path('carts/', cart_list, name='carts'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('payment/', payment, name='payment'),
    path('privacy/', privacy, name='privacy'),
    path('reward/', reward, name='reward'),
    path('invoice/<int:id>/', invoice, name='invoice'),

]
