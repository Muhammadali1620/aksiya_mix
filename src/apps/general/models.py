from django.db import models
from apps.general.services import normalize_slug, normalize_txt


class AbstractModel(models.Model):

    def save(self, *args, **kwargs):
        normalize_txt(self)
        normalize_slug(self)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True