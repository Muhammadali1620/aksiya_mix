from django.db import models
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify

from apps.general.models import AbstractModel


class Category(AbstractModel):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25, unique=True, blank=True)
    parent = models.ForeignKey(
        to='self',
        on_delete=models.PROTECT,
        related_name='children',
        blank=True,
        null=True)
    icon = models.ImageField(upload_to='category/icons/%Y/%m/%d/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.parent and not self.icon:
            raise ValidationError({'icon':'Category must have an icon'})

        try:
            if not self.pk and self.parent.parent.parent:
                raise ValidationError('Subcategory cannot have more than 3 levels')
        except AttributeError:
            pass

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name