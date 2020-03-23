from django.db import models

# Create your models here.

class Product():
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.PositiveIntegerField(max_length=20)
    stock = models.PositiveIntegerField(max_length=20)
    type = models.CharField(max_length=20)
    offer = models.CharField(max_length=50)
    delevery_charge = models.CharField(max_length=20)
    photo = models.FileField(upload_to=None, max_length=254, **options)
    free_delivery = models.BooleanField(default=False)


class ProductPhoto():
    product_id = models.Foreignkey(Product)
    image = models.FileField()


class Comment():
    user_id = models.Foreignkey()
    product_id = models.Foreignkey(Product)
    details = models.CharField(max_length=255)


class Card():
    user_id = models.Foreignkey()
    product_id = models.Foreignkey(Product)
