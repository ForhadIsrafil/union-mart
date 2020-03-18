import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _

try:
    from slugify import slugify
except ImportError:
    from django.utils.text import slugify


class UUIDable(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )

    class Meta:
        abstract = True


class Timestampable(models.Model):
    creation_date = models.DateTimeField(_("date created"), auto_now_add=True)
    modified_date = models.DateTimeField(_("date last modified"), auto_now=True)

    class Meta:
        abstract = True


class Slugable(models.Model):
    """
    An abstract behavior representing adding a unique slug to a model
    based on the slug_source property.
    """

    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super(Slugable, self).save(*args, **kwargs)

    def get_slug(self):
        return slugify(getattr(self, "slug_source"), to_lower=True)

    def is_unique_slug(self, slug):
        qs = self.__class__.objects.filter(slug=slug)
        return not qs.exists()

    def generate_unique_slug(self):
        slug = self.get_slug()
        new_slug = slug

        iteration = 1
        while not self.is_unique_slug(new_slug):
            new_slug = "%s-%d" % (slug, iteration)
            iteration += 1

        return new_slug
