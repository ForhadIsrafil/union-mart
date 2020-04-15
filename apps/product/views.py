from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from .models import Product, UpdateNews, Slider, Trend, ProductPhoto, Cart


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
    cart_count = Cart.objects.filter(user_id=request.user.id).count()

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
        'cart_count': cart_count if cart_count else 0,
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
                # 'price': price_filter_first,
            }
            return render(request, 'product.html', context)
        elif category:
            product_ins = product_ins.filter(Q(category=category) & Q(price__gte=price_filter[0]) & Q(price__lte=price_filter[1]))
            context = {
                'products': product_ins,
                'category': category,
                'sub_category': sub_category,
                # 'price': price_filter_first,

            }
            return render(request, 'product.html', context)
        else:
            product_ins = product_ins.filter(Q(sub_category=sub_category) & Q(price__gte=price_filter[0]) & Q(price__lte=price_filter[1]))
            context = {
                'products': product_ins,
                'category': category,
                'sub_category': sub_category,
                # 'price': price_filter_first,

            }
            return render(request, 'product.html', context)

    if search_product:
        # import pdb;
        # pdb.set_trace()
        strip_regex = search_product.strip()
        arr_regex = strip_regex.split(' ')
        str_regex = ''
        for element in arr_regex:
            str_regex += r'\b' + str(element) + r'\b|'
        str_regex = str_regex[:-1]
        if category and sub_category:
            product_ins = product_ins.filter(Q(category=category) & Q(sub_category=sub_category) & Q(description__iregex=r"" + str_regex + ""))
            context = {
                'products': product_ins,
                'category': category,
                'sub_category': sub_category,
                # 'price': price_filter_first,
            }
            return render(request, 'product.html', context)
        elif category:
            product_ins = product_ins.filter(Q(category=category) & Q(description__iregex=r"" + str_regex + ""))
            context = {
                'products': product_ins,
                'category': category,
                'sub_category': sub_category,
                # 'price': price_filter_first,

            }
            return render(request, 'product.html', context)
        else:
            product_ins = product_ins.filter(Q(sub_category=sub_category) & Q(description__iregex=r"" + str_regex + ""))
            context = {
                'products': product_ins,
                'category': category,
                'sub_category': sub_category,
                # 'price': price_filter_first,

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
        # 'price': price_filter_first,

    }
    return render(request, 'product.html', context)


def product_details(request, product_id):
    product_ins = Product.objects.filter(id=product_id).first()
    product_photo_ins = ProductPhoto.objects.filter(product_id=product_id).order_by('-id')

    quantity = request.GET.get('quantity_id')
    if quantity:
        check_card_ins = Cart.objects.filter(user_id=request.user.id, product_id=product_ins.id).exists()
        if not check_card_ins:
            card = Cart(user_id=request.user.id, product_id=product_ins.id, quantity=quantity)
            card.save()
            return JsonResponse({'valid': True, 'message': 'success.'})
        else:
            return JsonResponse({'valid': False, 'message': 'This product is already added.'})

    if product_ins:
        related_products = Product.objects.filter(category=product_ins.category, sub_category=product_ins.sub_category).exclude(id=product_ins.id).order_by('-upload_date')[:20]
        context = {
            'product_details': product_ins,
            'product_images': product_photo_ins,
            'related_products': related_products,
        }
        return render(request, 'product-detail.html', context)


def cart_list(request):
    cart_ins = Cart.objects.filter(user_id=request.user.id).order_by('-quantity')
    context = {
        'carts': cart_ins
    }
    delete_cart_id = request.GET.get('delete_cart_id')
    if delete_cart_id:
        cart_ins = cart_ins.filter(id=delete_cart_id).first()
        cart_ins.delete()
        # return JsonResponse({'valid': True, 'message': 'success.'})

    return render(request, 'shoping-cart.html', context)


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def header2(request):
    return render(request, 'header2.html', {})
