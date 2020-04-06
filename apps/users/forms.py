from apps.users.models import User
from django import forms
# from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm, UserCreationForm)
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.phonenumber import PhoneNumber, to_python


class UserFormValidationMixin(object):
    error_messages = {"password_mismatch": _("The two password fields didn't match.")}


class EmailFormMixin(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                _("Email '%(email)s' is already taken. "),
                params={"email": email},
                code="email_exists"
            )
        return email


class SignupForm(forms.ModelForm):
    # image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ("first_name", "user_name", "email", "password", "phone_number", "date_of_birth")

    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data["phone_number"]
    #     if not PhoneNumber.is_valid(to_python(phone_number)) or User.objects.filter(phone_number=phone_number).exists():
    #         return forms.ValidationError(_("The phone-number is not valid or already exist!"))


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages["invalid_login"] = _(
            "Please enter a correct %(username)s and password."
        )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "email", "image")


class DeleteAccountForm(forms.Form):
    accept = forms.BooleanField()


class UpdateUserInfoForm(forms.ModelForm):
    email = forms.EmailField(label=_("Email"), widget=forms.EmailInput, help_text=_("Enter the email of that User"), )

    class Meta:
        model = User
        fields = (
            "first_name", "last_name", "email", "image", "password",)

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data["password"]
        if password:
            user.set_password(password)
            if commit:
                user.save()
        return user


class AdminUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class AdminUserCreationForm(UserCreationForm, UserFormValidationMixin):
    email = forms.EmailField(
        label=_("Email"),
        widget=forms.EmailInput,
        help_text=_("Enter the email of that User"),
    )

    class Meta:
        model = User
        fields = ("email",)

    def save(self, commit=True):
        user = super(AdminUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.set_to_user()

        if commit:
            user.save()

        return user
