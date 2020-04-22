from django.conf import settings as app_settings

from .models import Cart


# def count_cart(request):
#     count_carts = Cart.objects.filter(user_id=request.user.id).count()
#     return count_carts if count_carts else 0


def count_cart(request):
    return {"cart_count": app_settings.CART_COUNT + Cart.objects.filter(user_id=request.user.id).count()}
