from apps.users.views import User
from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    type = models.CharField(max_length=20)
    offer = models.CharField(max_length=50)
    delevery_charge = models.CharField(max_length=20)
    photo = models.FileField(upload_to=None, max_length=254)  # **options
    free_delivery = models.BooleanField(default=False)


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, related_name='+', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/product_image')


# class Comment(models.Model):
#     user_id = models.Foreignkey()
#     product_id = models.Foreignkey(Product)
#     details = models.CharField(max_length=255)


class Card(models.Model):
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='+', on_delete=models.CASCADE)
