from apps.product.models import Product, ProductPhoto, Slider, UpdateNews
from django.contrib import admin


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductPhotoInline,)
    list_display = ('name', 'price', 'stock', 'category',)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title')


@admin.register(UpdateNews)
class UpdateNewsAdmin(admin.ModelAdmin):
    list_display = ('news',)
