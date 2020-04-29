from apps.product.models import Product, ProductPhoto, Slider, UpdateNews, Trend, PaymentPhoneNumber, OrderPayment, Reward, \
    SocialLink
from django.contrib import admin


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductPhotoInline,)
    list_display = ('name', 'price', 'stock', 'category', 'sub_category', 'stock', 'upload_date',)
    search_fields = ('id', 'name', 'category', 'sub_category', 'trend_name',)
    list_filter = ('id', 'name', 'category', 'sub_category',)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title')


@admin.register(UpdateNews)
class UpdateNewsAdmin(admin.ModelAdmin):
    list_display = ('news',)


@admin.register(Trend)
class TrendAdmin(admin.ModelAdmin):
    list_display = ('trend_name', 'image', 'position')


@admin.register(PaymentPhoneNumber)
class PaymentPhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('payment_gateway', 'phone_number',)


@admin.register(OrderPayment)
class OrderPaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'invoice_no', 'delivery_location', 'contact_number',)
    search_fields = ('id', 'user', 'invoice_no', 'contact_number',)
    readonly_fields = ('user', 'invoice_no', 'product_list', 'delivery_location', 'contact_number', 'payment_number',
                       'delivery_charge', 'total', 'order_date', 'city', 'payment_gateway')
    list_filter = ('id', 'user', 'invoice_no', 'contact_number',)
    # def get_readonly_fields(self, request, obj=None):
    #     return [f.name for f in self.model._meta.fields]

    # def has_change_permission(self, request, obj=None):
    #     return False


@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ('reward_title', 'position',)


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('facebook', 'twitter', 'youtube', 'instagram', 'contact_mail',
                    'information_mail', 'customer_care', 'complain_suggestion',)
