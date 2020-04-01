"""union_mart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('apps.product.urls')),
    path('users/', include('apps.users.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
from django.urls import path
from apps.users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", user_views.LoginView.as_view(), name="login"),

    path("signup/", user_views.SignupView.as_view(), name="signup"),

    path("verify-email/", user_views.verify_email, name="verify_email"),

]
>>>>>>> ecf13ffb53a260d550d120a6c1a2a6bbf5f8d645
