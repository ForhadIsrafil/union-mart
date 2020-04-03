from apps.users.views import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    name = models.CharField(verbose_name=_('Product Name'), max_length=255)
    description = models.TextField(max_length=255)
    price = models.PositiveIntegerField(verbose_name=_('Product Price'))
    stock = models.PositiveIntegerField(verbose_name=_('Stock of Products'))
    type = models.CharField(verbose_name=_('Product Type'), max_length=20)
    offer = models.CharField(max_length=50)
    delevery_charge = models.CharField(max_length=20)
    # default_photo = models.FileField(upload_to='product_image', max_length=254)  # **options
    free_delivery = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse(
            "exercise_detail",
            # args=[self.chapter.course.slug, self.chapter.position, self.position],
            args=[self.id],
        )


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, related_name='+', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product-images')

    class Meta:
        verbose_name = _("Product Photo")
        verbose_name_plural = _("Product Photos")

    def __str__(self):
        return f"{self.product.id} - {self.product.name}"


# class Comment(models.Model):
#     user_id = models.Foreignkey()
#     product_id = models.Foreignkey(Product)
#     details = models.CharField(max_length=255)


class Card(models.Model):
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='+', on_delete=models.CASCADE)
