from django.db.models import Q
from django.shortcuts import render

from .models import Product, UpdateNews, Slider, Trend, ProductPhoto


def home(request):
    slider_ins = Slider.objects.all().order_by('-id')
    product_ins = Product.objects.all().order_by('-upload_date')
    updated_news_ins = UpdateNews.objects.all().order_by('-id')
    trend_ins = Trend.objects.all().order_by('-id')
    women_ins = product_ins.filter(category='Women')[:3]
    men_ins = product_ins.filter(category='Men')[:3]
    bag_ins = product_ins.filter(sub_category='Bag')[:3]
    shoe_ins = product_ins.filter(sub_category='Shoe')[:3]
    watch_ins = product_ins.filter(sub_category='Watch')[:3]

    context = {
        'products': product_ins,
        'sliders': slider_ins,
        'updated_news': updated_news_ins,
        'trends': trend_ins,
        'womens': women_ins,
        'mens': men_ins,
        'bags': bag_ins,
        'shoes': shoe_ins,
        'watches': watch_ins,
    }
    return render(request, 'index.html', context)


def product(request):
    category = request.GET.get('category', None)
    sub_category = request.GET.get('sub_category', None)
    search_product = request.POST.get('search_product', None)
    price_filter_first = request.GET.get('price', None)

    product_ins = Product.objects.all().order_by('-upload_date')

    if price_filter_first:
        price_filter = price_filter_first.split('-')
        if category and sub_category:
            product_ins = product_ins.filter(Q(category=category) & Q(sub_category=sub_category) & Q(price__gte=price_filter[0]) & Q(price__lte=price_filter[1]))
            context = {
                'products': product_ins,
                'category': category,
                'sub_category': sub_category,
                'price': price_filter_first,
            }
            return render(request, 'product.html', context)
        elif category:
            product_ins = product_ins.filter(Q(category=category) & Q(price__gte=price_filter[0]) & Q(price__lte=price_filter[1]))
            context = {
                'products': product_ins,
                'category': category,
                'sub_category': sub_category,
                'price': price_filter_first,

            }
            return render(request, 'product.html', context)
        else:
            product_ins = product_ins.filter(Q(sub_category=sub_category) & Q(price__gte=price_filter[0]) & Q(price__lte=price_filter[1]))
            context = {
                'products': product_ins,
                'category': category,
                'sub_category': sub_category,
                'price': price_filter_first,

            }
            return render(request, 'product.html', context)

    if search_product:
        if category and sub_category:
            product_ins = product_ins.filter(Q(category=category) & Q(sub_category=sub_category) & Q(description__icontains=search_product))
            context = {
                'products': product_ins,
                'category': category,
                'sub_category': sub_category,
                'price': price_filter_first,
            }
            return render(request, 'product.html', context)
        elif category:
            product_ins = product_ins.filter(Q(category=category) & Q(description__icontains=search_product))
            context = {
                'products': product_ins,
                'category': category,
                'sub_category': sub_category,
                'price': price_filter_first,

            }
            return render(request, 'product.html', context)
        else:
            product_ins = product_ins.filter(Q(sub_category=sub_category) & Q(description__icontains=search_product))
            context = {
                'products': product_ins,
                'category': category,
                'sub_category': sub_category,
                'price': price_filter_first,

            }
            return render(request, 'product.html', context)

    if category and sub_category:
        product_ins = product_ins.filter(Q(category=category) & Q(sub_category=sub_category))
    elif category:
        product_ins = product_ins.filter(category=category)
    elif sub_category:
        product_ins = product_ins.filter(sub_category=sub_category)

    else:
        product_ins = product_ins

    context = {
        'products': product_ins,
        'category': category,
        'sub_category': sub_category,
        'price': price_filter_first,

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
