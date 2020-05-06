from apps.users.views import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from jsonfield import JSONField


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Constructions', 'Constructions'),
        ('Home Decorations', 'Home Decorations'),
        ('Electronics', 'Electronics'),
        ('Others', 'Others'),
        ('Kids World', 'Kids World')
    )

    SUB_CATEGORY_CHOICES = (
        ('Watch', 'Watch'),
        ('Belt', 'Belt'),
        ('Wallet', 'Wallet'),
        ('Shoe', 'Shoe'),
        ('Sunglass', 'Sunglass'),
        ('Ornaments', 'Ornaments'),
        ('Phrase', 'Phrase'),
        ('Safety Equipments', 'Safety Equipments'),
        ('Tools', 'Tools'),
        ('Machinery', 'Machinery'),
        ('Hardware', 'Hardware'),
        ('Sanitary', 'Sanitary'),
        ('Washing Device', 'Washing Device'),
        ('Water Purifiers', 'Water Purifiers'),
        ('Kitchen & Cleaning', 'Kitchen & Cleaning'),
        ('CC Camera', 'CC Camera'),
        ('Earphone', 'Earphone'),
        ('Scale', 'Scale'),
        ('Storage Device', 'Storage Device'),
        ('Network Device', 'Network Device'),
        ('Health Caret', 'Health Care'),
        ('Stationery', 'Stationery'),
        ('Rain Coat', 'Rain Coat'),
        ('Kids Toys', 'Kids Toys'),
        ('Bag', 'Bag'),
    )

    name = models.CharField(verbose_name=_('Product Name'), max_length=255)
    description = models.TextField(max_length=255)
    price = models.PositiveIntegerField(verbose_name=_('Product Price'))
    stock = models.PositiveIntegerField(verbose_name=_('Stock of Products'))
    category = models.CharField(choices=CATEGORY_CHOICES, verbose_name=_('Product Category'), max_length=20,
                                default=CATEGORY_CHOICES[0])
    sub_category = models.CharField(choices=SUB_CATEGORY_CHOICES, verbose_name=_('Product Sub-Category'), max_length=20,
                                    default=SUB_CATEGORY_CHOICES[0])
    offer = models.CharField(max_length=50, null=True, blank=True)
    # delevery_charge = models.CharField(max_length=20, null=True, blank=True)
    default_photo = models.ImageField(upload_to='default_photo', help_text=mark_safe('<h2 style="color: #008CBA;">Images size must be height: 1200px and width: 1486px format.</h2>'))  # size must be ato ato pixel
    # free_delivery = models.BooleanField(default=False)
    upload_date = models.DateField(auto_now_add=True)
    trend_name = models.CharField(max_length=50, null=True, blank=True)
    discount = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


@receiver(post_delete, sender=Product)
def submission_delete(sender, instance, **kwargs):
    instance.default_photo.delete(False)


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, related_name='+', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images', help_text=mark_safe('<h2 style="color: #008CBA;">Images size must be height: 1200px and width: 1486px format.</h2><br>Can add only 3 images please.'))

    class Meta:
        verbose_name = _("Product Photo")
        verbose_name_plural = _("Product Photos")

    def __str__(self):
        return f"{self.product.id} - {self.product.name}"

    def clean(self, *args, **kwargs):
        super(ProductPhoto, self).save(*args, **kwargs)
        qs = ProductPhoto.objects.all()
        if qs.count() > 3 :
            qs.last().delete()
            raise ValidationError('Can not add more row. Can add only 3 images please.')


@receiver(post_delete, sender=ProductPhoto)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class Cart(models.Model):
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='+', on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")


class Slider(models.Model):
    title = models.CharField(max_length=40)
    sub_title = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='slider_image', help_text=mark_safe('<h2 style="color: #008CBA;">Images size must be height: 1920px and width: 930px format.Can add only 3 rows.</h2>'))
    position = models.PositiveSmallIntegerField()
    product_id = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = _("Slider")
        verbose_name_plural = _("Slider")

    def __str__(self):
        return self.title

    def clean(self, *args, **kwargs):
        super(Slider, self).save(*args, **kwargs)
        qs = Slider.objects.all()
        if qs.count() > 3 :
            qs.last().delete()
            raise ValidationError('Can not add more row. Can add only 3 rows please.')


@receiver(post_delete, sender=Slider)
def submission_delete(sender, instance, **kwargs):
    instance.photo.delete(False)


class UpdateNews(models.Model):
    news = models.CharField(max_length=100)
    position = models.PositiveSmallIntegerField(null=True)

    class Meta:
        verbose_name = _("Updated News")
        verbose_name_plural = _("Updated News")

    def __str__(self):
        return self.news

    def clean(self, *args, **kwargs):
        super(UpdateNews, self).save(*args, **kwargs)
        qs = UpdateNews.objects.all()
        if qs.count() > 2:
            qs.last().delete()
            raise ValidationError('Can not add more row. Can add only 2 rows please.')


class Trend(models.Model):
    trend_name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='trend_images', help_text=mark_safe('<h2 style="color: #008CBA;">Images size must be height: 1200px and width: 809px format.Can not add more row. Can add only 4 rows.</h2>'))
    position = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = _("Trend")
        verbose_name_plural = _("Trends")

    def __str__(self):
        return self.trend_name

    def clean(self, *args, **kwargs):
        super(Trend, self).save( *args, **kwargs)
        qs = Trend.objects.all()
        if qs.count() > 4:
            qs.last().delete()
            raise ValidationError('Can not add more row. Can add only 4 trends please.')


@receiver(post_delete, sender=Trend)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class SocialLink(models.Model):
    facebook = models.URLField(max_length=250)
    twitter = models.URLField(max_length=250)
    youtube = models.URLField(max_length=250)
    instagram = models.URLField(max_length=250)
    contact_mail = models.EmailField(max_length=120)
    information_mail = models.EmailField(max_length=250)
    customer_care = models.URLField(max_length=250)
    complain_suggestion = models.URLField(max_length=250)
    order_confirmation = models.URLField(max_length=250)

    class Meta:
        verbose_name = _("Social Link")
        verbose_name_plural = _("Social Links")

    def __str__(self):
        return self.facebook

    def clean(self, *args, **kwargs):
        super(SocialLink, self).save(*args, **kwargs)
        qs = SocialLink.objects.all()
        if qs.count() > 1:
            qs.last().delete()
            raise ValidationError('Can not add more row. Can add only 1 rows please.')


class Review(models.Model):
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='+', on_delete=models.CASCADE)
    description = models.TextField()


class PaymentPhoneNumber(models.Model):
    SERVICE_NAME_CHOICES = (("Bkash", "Bkash"), ("Rocket", "Rocket"), ("Nagad", "Nagad"),)

    phone_number = models.CharField(help_text="Phone Number.", null=True, blank=True, max_length=11, )
    payment_gateway = models.CharField(max_length=20, choices=SERVICE_NAME_CHOICES, default=SERVICE_NAME_CHOICES[0])
    image = models.ImageField(upload_to="service_image", help_text=mark_safe('<h2 style="color: #008CBA;">Images size must be height: 150px and width: 300px format.</h2><br>'))

    class Meta:
        verbose_name = _("Payment Phone Number")
        verbose_name_plural = _("Payment Phone Numbers")

    def __str__(self):
        return self.payment_gateway

    def clean(self, *args, **kwargs):
        super(PaymentPhoneNumber,self).save(*args, **kwargs)
        qs = PaymentPhoneNumber.objects.all()
        if qs.count() > 3:
            qs.last().delete()
            raise ValidationError('Can not add more row. Can add only 3 rows please.')


@receiver(post_delete, sender=PaymentPhoneNumber)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class OrderPayment(models.Model):
    def number():
        no = OrderPayment.objects.count()
        if no is None:
            return 1
        else:
            return no + 1

    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    invoice_no = models.PositiveIntegerField(unique=True, default=number)
    product_list = JSONField()
    delivery_location = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=11)
    payment_number = models.CharField(max_length=11, null=True, blank=True)
    delivery_charge = models.CharField(max_length=50, default='Depends on courier.')
    total = models.CharField(max_length=255)
    order_date = models.DateField(auto_now_add=True)
    city = models.CharField(max_length=20)
    payment_gateway = models.CharField(max_length=50, default='Cash on delivery.', editable=False)
    is_delivered = models.BooleanField(default=False, help_text=_('Is products are delivered?'))

    class Meta:
        verbose_name = _("Order and Payment")
        verbose_name_plural = _("Order and Payments")

    def __str__(self):
        return self.payment_gateway

    # def save(self, *args, **kwargs):
    #     if self.payment_gateway is None:
    #         self.payment_gateway = 'Cash on delivery.'
    #     return super(OrderPayment, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product:invoice', args=[self.id])


class Reward(models.Model):
    image = models.ImageField(upload_to='reward_images', help_text=mark_safe('<h2 style="color: #008CBA;">Images size must be height: 308px and width: 184px format.Can add only 4 rows.</h2><br>'))
    reward_title = models.CharField(max_length=50, null=True, blank=True, verbose_name='Reward Title')
    position = models.PositiveSmallIntegerField(null=True)

    def clean(self, *args, **kwargs):
        super(Reward, self).save(*args, **kwargs)
        qs = Reward.objects.all()
        if qs.count() > 4:
            qs.last().delete()
            raise ValidationError('Can not add more row.Can add only 4 rows please.')


@receiver(post_delete, sender=Reward)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)
