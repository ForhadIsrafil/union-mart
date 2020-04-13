from apps.product.models import Product, ProductPhoto, Slider, UpdateNews, Trend
from django.contrib import admin


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductPhotoInline,)
    list_display = ('name', 'price', 'stock', 'category', 'sub_category', 'stock', 'upload_date',)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title')


@admin.register(UpdateNews)
class UpdateNewsAdmin(admin.ModelAdmin):
    list_display = ('news',)


@admin.register(Trend)
class TrendAdmin(admin.ModelAdmin):
    list_display = ('trend_name', 'image', 'position')
