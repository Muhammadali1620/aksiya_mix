from django.db import models

from apps.general.models import AbstractModel


class Service(AbstractModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    icon = models.ImageField(upload_to='discount/icon/%Y/%m/%d/', blank=True, null=True)

    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name