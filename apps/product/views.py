import datetime
import json
import time
import os
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib import messages
from django.db.models import Count, Q
from django.db import models, transaction
from django.http import JsonResponse, Http404, HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, RedirectView, TemplateView, View
from django.views.generic.base import ContextMixin, TemplateResponseMixin
from .models import Product, Card, ProductPhoto, UpdateNews, Slider


def home(request):
    slider_ins = Slider.objects.all().order_by('-id')
    product_ins = Product.objects.all().order_by('-upload_date')
    context = {
        'products': product_ins,
        'sliders': slider_ins
    }
    return render(request, 'index.html', context)


def product(request):
    return render(request, 'product.html', {})


def product_details(request):
    return render(request, 'product-detail.html', {})


def shoping_cart(request):
    return render(request, 'shoping-cart.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})
