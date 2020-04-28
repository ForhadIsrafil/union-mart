from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage


def pagination(product_ins, page):
    paginator = Paginator(product_ins, 1)
    try:
        product_ins = paginator.page(page)
    except PageNotAnInteger:
        product_ins = paginator.page(1)
    except (EmptyPage, InvalidPage):
        product_ins = paginator.page(paginator.num_pages)
    return product_ins
