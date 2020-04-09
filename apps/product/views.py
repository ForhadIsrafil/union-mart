from django.shortcuts import render

from .models import Product, UpdateNews, Slider, Trend, ProductPhoto


def home(request):
    slider_ins = Slider.objects.all().order_by('-id')
    product_ins = Product.objects.all().order_by('-upload_date')
    updated_news_ins = UpdateNews.objects.all().order_by('-id')
    trend_ins = Trend.objects.all().order_by('-id')
    women_ins = product_ins.filter(category='Women')[:3]
    context = {
        'products': product_ins,
        'sliders': slider_ins,
        'updated_news': updated_news_ins,
        'trends': trend_ins,
        'womens': women_ins,
    }
    return render(request, 'index.html', context)


def product(request):
    product_ins = Product.objects.all().order_by('-id')
    context = {
        'products': product_ins
    }
    return render(request, 'product.html', context)


def product_details(request, product_id):
    product_ins = Product.objects.filter(id=product_id).first()
    product_photo_ins = ProductPhoto.objects.filter(product_id=product_id).order_by('-id')

    context = {
        'product_details': product_ins,
        'product_images': product_photo_ins,
    }
    return render(request, 'product-detail.html', context)


def shoping_cart(request):
    return render(request, 'shoping-cart.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})
