from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def product(request):
    return render(request, 'product.html', {})


def product_details(request):
    return render(request, 'product-detail.html', {})


def shoping_cart(request):
    return render(request, 'shoping-cart.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})
