from apps.users.views import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


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
    category = models.CharField(choices=CATEGORY_CHOICES, verbose_name=_('Product Category'), max_length=20, default=CATEGORY_CHOICES[0])
    sub_category = models.CharField(choices=SUB_CATEGORY_CHOICES, verbose_name=_('Product Sub-Category'), max_length=20, default=SUB_CATEGORY_CHOICES[0])
    offer = models.CharField(max_length=50, null=True, blank=True)
    delevery_charge = models.CharField(max_length=20, null=True, blank=True)
    default_photo = models.ImageField(upload_to='default_photo', help_text="size must be ato ato pixel.")  # size must be ato ato pixel
    free_delivery = models.BooleanField(default=False)
    upload_date = models.DateField(auto_now_add=True)
    trend_name = models.CharField(max_length=50, null=True, blank=True)
    discount = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse(
            "product:product",
            # args=[self.chapter.course.slug, self.chapter.position, self.position],
            args=[self.id],
        )


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, related_name='+', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')

    class Meta:
        verbose_name = _("Product Photo")
        verbose_name_plural = _("Product Photos")

    def __str__(self):
        return f"{self.product.id} - {self.product.name}"


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
    photo = models.ImageField(upload_to='slider_image')

    class Meta:
        verbose_name = _("Slider")
        verbose_name_plural = _("Slider")

    def __str__(self):
        return self.title


class UpdateNews(models.Model):
    news = models.CharField(max_length=100)
    position = models.PositiveSmallIntegerField(null=True)

    class Meta:
        verbose_name = _("Updated News")
        verbose_name_plural = _("Updated News")

    def __str__(self):
        return self.news


class Trend(models.Model):
    trend_name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='trend_images')
    position = models.PositiveSmallIntegerField(null=True)

    class Meta:
        verbose_name = _("Trend")
        verbose_name_plural = _("Trends")

    def __str__(self):
        return self.trend_name


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


class Review(models.Model):
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='+', on_delete=models.CASCADE)
    description = models.TextField()


class PaymentPhoneNumber(models.Model):
    SERVICE_NAME_CHOICES = (("Bkash", "Bkash"), ("Rocket", "Rocket"), ("Nagad", "Nagad"),)

    phone_number = models.PositiveSmallIntegerField(help_text="Phone Number.", max_length=11, null=True, blank=True)
    service_name = models.CharField(max_length=20, choices=SERVICE_NAME_CHOICES, default=SERVICE_NAME_CHOICES[0])
    image = models.ImageField(upload_to="service_image")

    class Meta:
        verbose_name = _("Payment Phone Number")
        verbose_name_plural = _("Payment Phone Numbers")

    def __str__(self):
        return self.service_name

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse(
            "product:invoice",
            # args=[self.chapter.course.slug, self.chapter.position, self.position],
            # args=[self.id],
        )
