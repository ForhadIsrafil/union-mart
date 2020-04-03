from apps.product.models import Product, ProductPhoto, Card
from django.contrib import admin
import nested_admin
import csv
from io import StringIO

from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductPhotoInline,)
    list_display = ('name', 'price', 'stock', 'type',)
