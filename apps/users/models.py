from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import cached_property
from django.utils import timezone
from apps.core.lib.behaviors import UUIDable, Timestampable
# from apps.core.storages import DownloadableS3Boto3Storage
# from .upload_to import user_image_upload_path

# from .random_images import data
from random import randrange


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if email is None:
            raise ValueError(_("The email must be set"))

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        if password is None:
            raise TypeError(_("Superusers must have a password."))

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    # image = models.ImageField(
    #     _("image"), blank=True, null=True, upload_to=user_image_upload_path)

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    nickname = models.CharField(max_length=20, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    objects = UserManager()

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
