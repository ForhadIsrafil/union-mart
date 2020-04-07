import json

from apps.users.models import User
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.views.generic import FormView, TemplateView, UpdateView, View

from .forms import (DeleteAccountForm, LoginForm, SignupForm, )


class SignupView(FormView):
    template_name = "users/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        # import pdb;pdb.set_trace()
        user = form.save(commit=False)
        user.is_active = True
        user.phone_number = '+88' + form.cleaned_data["phone_number"]
        user.set_password(form.cleaned_data["password"])
        user.save()
        # login(self.request, user)
        next_url = self.request.GET.get("next")
        # if next_url:
        #     return HttpResponseRedirect(next_url)

        messages.add_message(
            self.request,
            messages.INFO,
            _(
                "Your account successfully created! And enjoy shopping!"
            ),
        )
        return super().form_valid(form)


class LoginView(FormView):
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("product:product")

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
        # import pdb;pdb.set_trace()
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
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                next_url = self.request.GET.get("next")

                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    return redirect(self.success_url)
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


class PasswordResetView(auth_views.PasswordResetView):  # it's meaning forgot password , get email and send acivation-mail
    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        # import pdb;pdb.set_trace()
        email = self.request.POST.get('email')
        user_email = User.objects.filter(email=email).values('email')
        user_email = user_email[0]['email'] if user_email else user_email
        self.request.POST._mutable = True
        self.request.POST['email'] = user_email
        return super().dispatch(*args, **kwargs)


class DashboardView(TemplateView):  # LoginRequiredMixin
    template_name = "users/dashboard.html"
