import math

from .models import Cart


def product_total_amount(user):
    cart_ins = Cart.objects.filter(user_id=user.id).order_by('-quantity')
    product_arr = []
    total_price = 0
    if user.has_discount:
        for cart in cart_ins:
            temp = {}
            temp['product_id'] = cart.product.id
            temp['name'] = cart.product.name
            temp['price'] = cart.product.price
            temp['default_photo_url'] = cart.product.default_photo.url
            temp['quantity'] = cart.quantity
            temp['discount'] = user.discount
            if user.discount:
                per_discount_tk = cart.product.price * user.discount / 100
                # print('per_discount_tk ', per_discount_tk)
                total_discount = cart.quantity * per_discount_tk
                # print('total_discount ', total_discount)

                temp['per_total'] = (cart.product.price * cart.quantity) - math.floor(total_discount)
                # print(' total ', (cart.product.price * cart.quantity) - total_discount)

                total_price += (cart.product.price * cart.quantity) - math.floor(total_discount)
                # print('total_price 1111 ', total_price)

            else:
                temp['per_total'] = cart.product.price * cart.quantity
                total_price += cart.product.price * cart.quantity
                # print('total_price ', total_price)
            product_arr.append(temp)

        return {'products': product_arr, 'total_price': total_price, }

    for cart in cart_ins:
        temp = {}
        temp['product_id'] = cart.product.id
        temp['name'] = cart.product.name
        temp['price'] = cart.product.price
        temp['default_photo_url'] = cart.product.default_photo.url
        temp['quantity'] = cart.quantity
        temp['discount'] = cart.product.discount
        if cart.product.discount:
            per_discount_tk = cart.product.price * cart.product.discount / 100
            # print('per_discount_tk ', per_discount_tk)
            total_discount = cart.quantity * per_discount_tk
            # print('total_discount ', total_discount)

            temp['per_total'] = (cart.product.price * cart.quantity) - math.floor(total_discount)
            # print(' total ', (cart.product.price * cart.quantity) - total_discount)

            total_price += (cart.product.price * cart.quantity) - math.floor(total_discount)
            # print('total_price 1111 ', total_price)

        else:
            temp['per_total'] = cart.product.price * cart.quantity
            total_price += cart.product.price * cart.quantity
            # print('total_price ', total_price)
        product_arr.append(temp)

    return {'products': product_arr, 'total_price': total_price, }
