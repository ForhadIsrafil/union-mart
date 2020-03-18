import re

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
)
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class UserFormValidationMixin(object):
    error_messages = {"password_mismatch": _("The two password fields didn't match.")}


class UserNameFormMixin(forms.Form):
    user_name = forms.CharField(max_length=60)

    def clean_user_name(self):
        user_name = self.cleaned_data["user_name"]

        # We restrict user_name/subdomain to only have
        # letters, numbers, and hyphens
        # we also do not allow usernames that start or end
        # with a hyphen, as well as succeeding hyphens
        if "--" in user_name or not re.match(
                r"^([a-zA-Z0-9][-a-zA-Z0-9]*)(?<!-)$", user_name
        ):
            raise forms.ValidationError(
                _(
                    "Invalid username, it can only contain letters, numbers and hyphen."
                    " It must not start or end with hyphen and must not contain"
                    " succeeding hyphens (--)."
                ),
                code="invalid_user_name",
            )

        if User.objects.filter(user_name__iexact=user_name).exists():
            raise forms.ValidationError(
                _("Username '%(user_name)s' is already taken."),
                params={"user_name": user_name},
                code="user_name_exists",
            )
        return user_name


class UserNameChangeFormMixin(forms.Form):
    user_name = forms.CharField(max_length=60)

    def clean_user_name(self):
        user_name = self.cleaned_data["user_name"]

        # We restrict user_name/subdomain to only have
        # letters, numbers, and hyphens
        # we also do not allow usernames that start or end
        # with a hyphen, as well as succeeding hyphens
        if "--" in user_name or not re.match(
                r"^([a-zA-Z0-9][-a-zA-Z0-9]*)(?<!-)$", user_name
        ):
            raise forms.ValidationError(
                _(
                    "Invalid username, it can only contain letters, numbers and hyphen."
                    " It must not start or end with hyphen and must not contain"
                    " succeeding hyphens (--)."
                ),
                code="invalid_user_name",
            )
        return user_name


class AdminUserChangeForm(UserChangeForm, UserNameChangeFormMixin):
    class Meta(UserChangeForm.Meta):
        model = User


class AdminUserCreationForm(UserCreationForm, UserFormValidationMixin, UserNameFormMixin):
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


class VerifyUserNameForm(UserNameFormMixin):
    pass


class VerifyEmailForm(EmailFormMixin):
    pass


class SignupForm(UserNameFormMixin, UserFormValidationMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ("user_name", "email", "password")


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages["invalid_login"] = _(
            "Please enter a correct %(username)s and password."
        )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "image")


class DeleteAccountForm(forms.Form):
    accept = forms.BooleanField()


class UpdateUserInfoForm(forms.ModelForm):
    email = forms.EmailField(label=_("Email"), widget=forms.EmailInput, help_text=_("Enter the email of that User"), )

    class Meta:
        model = User
        fields = (
            "first_name", "last_name", "email", "image", "password", "nickname", "public_name", "bio", "website",
            "role")

    def save(self, commit=True):
        import pdb;pdb.set_trace()
        user = super().save(commit=False)
        password = self.cleaned_data["password"]
        if password:
            user.set_password(password)
            if commit:
                user.save()
        return user
