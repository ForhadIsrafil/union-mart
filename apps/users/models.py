from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, user_name, password, **extra_fields):
        if email is None:
            raise ValueError(_("The email must be set"))
        if user_name is None:
            raise ValueError(_("The user_name must be set"))

        user = self.model(email=email, user_name=user_name, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_user(self, email, user_name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        return self._create_user(email, user_name, password, **extra_fields)

    def create_superuser(self, email, user_name, password, **extra_fields):
        if password is None:
            raise TypeError(_("Superusers must have a password."))

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self._create_user(email, user_name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=10)
    last_name = models.CharField(_('last name'), max_length=10, blank=True)
    user_name = models.CharField(_("user name"), max_length=20, blank=True, unique=True,
                                 help_text=_("User name can only contain letters, numbers and hyphen."))
    date_of_birth = models.DateField(null=True, blank=True)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    # image = models.ImageField(_("image"), blank=True, null=True, upload_to="media/profile_image/")
    phone_number = models.CharField(max_length=11)
    discount = models.SmallIntegerField(blank=True, null=True)

    objects = UserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.get_full_name() or self.email

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def set_to_user(self):
        self.is_staff = False
        self.is_superuser = False
        self.is_active = True

    @cached_property
    def has_discount(self):
        if self.discount:
            return True
        else:
            return False
