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
    path('payment/', order_payment, name='order_payment'),
    path('privacy/', privacy, name='privacy'),
    path('invoice/<int:id>/', invoice, name='invoice'),
    path('footer/', footer, name='footer'),
    path('not-found/', notfound, name='not_found'),
    path('rewards/', reward, name='rewards'),
    path('how-to-buy/', howtobuy, name='how_to_buy'),


]
