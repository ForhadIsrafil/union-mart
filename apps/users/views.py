import json
import io
from datetime import datetime
import requests
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView
from django.contrib.sites.shortcuts import get_current_site
from django.core.files.storage import default_storage
from django.core.mail import EmailMessage
from django.db import models, transaction
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.generic import FormView, TemplateView, UpdateView, View
from django.contrib.sessions.models import Session

from apps.users.models import User
from .forms import (DeleteAccountForm, LoginForm, SignupForm, UpdateUserInfoForm, )


# User = get_user_model()

class SignupView(FormView):
    template_name = "users/login-signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = SignupForm(data=self.request.POST)
        if user.is_valid():
            user.is_active = True
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(self.request, user)
            next_url = self.request.GET.get("next")
            if next_url:
                return HttpResponseRedirect(next_url)
        else:
            return render(self.request, self.template_name, {'form': user.errors})

        messages.add_message(
            self.request,
            messages.INFO,
            _(
                "Your account successfully created! And enjoy shopping!"
            ),
        )
        return super().form_valid(form)


class LoginView(FormView):
    template_name = "users/login-signup"
    form_class = LoginForm
    success_url = reverse_lazy("projects")

    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url:
            return next_url
        return super().get_success_url()

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            return HttpResponse(json.dumps({"error": "invalid email or password"}))

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        if username:
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                messages.error(request, "Invalid Email ")
                return render(request, self.template_name, {"form": LoginForm})
        else:
            try:
                user = User.objects.get(user_name=username)
            except User.DoesNotExist:
                messages.error(request, "Invalid Username")
                return render(request, self.template_name, {"form": LoginForm})
        if user.check_password(password):
            if not user.is_active:
                user.is_active = True
                user.save()
            if user.is_active:
                login(request, user)
                next_url = self.request.GET.get("next")

                if next_url:
                    return HttpResponseRedirect(next_url)
            else:
                messages.error(
                    request,
                    "Please use correct credential to login.",
                )
                return render(request, self.template_name, {"form": LoginForm})
        else:
            messages.error(request, "Invalid Password")
            return render(request, self.template_name, {"form": LoginForm})

    def get(self, request, *args, **kwargs):
        if bool(request.GET.get("signup", None)):
            messages.add_message(
                request,
                messages.INFO,
                "Signup successfully completed! Please login.",
            )
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.user_cache)
        return super().form_valid(form)


@login_required
class UserProfileView(UpdateView):
    model = User
    fields = ("first_name", "last_name", "email")
    template_name = "users/profile.html"
    success_url = reverse_lazy("user_profile")

    def get_object(self):
        return self.request.user

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["first_name"].required = True
        form.fields["last_name"].required = False
        return form

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, "Profile successfully updated."
        )
        return super().form_valid(form)


@login_required
class UploadProfileImageView(View):
    def post(self, request, *args, **kwargs):
        user = self.request.user
        image = request.FILES["image"]
        file_name = request.POST["file_name"]

        user.image = image
        user.save()

        if self.request.is_ajax():
            return JsonResponse({}, status=200)
        return super().post(request, *args, **kwargs)


@login_required
class ChangePasswordView(PasswordChangeView):  # changing existing password
    template_name = "users/change_password.html"
    success_url = reverse_lazy("change_password")

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, "Password successfully changed."
        )
        return super().form_valid(form)


@login_required
class DeleteAccountView(FormView):
    template_name = "users/delete_account.html"
    form_class = DeleteAccountForm
    success_url = reverse_lazy("signup")

    @transaction.atomic
    def form_valid(self, form):
        self.request.user.delete()
        logout(self.request)
        messages.add_message(
            self.request,
            messages.INFO,
            "Account deleted. You may signup again for a new account.",
        )
        return super().form_valid(form)


def logoutUser(request):
    logout(request)
    request.session.flush()
    return redirect('/')


class PasswordResetView(auth_views.PasswordResetView):  # it's meaning forgot password , get email and send mail
    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        email = self.request.POST.get('email')
        user_email = User.objects.filter(Q(email=email) | Q(user_name=email)).values('email')
        user_email = user_email[0]['email'] if user_email else user_email
        self.request.POST._mutable = True
        self.request.POST['email'] = user_email
        return super().dispatch(*args, **kwargs)


class DashboardView(TemplateView):  # LoginRequiredMixin
    template_name = "users/dashboard.html"
