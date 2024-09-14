from django.db import models
from apps.general.services import normalize_txt


class AbstractModel(models.Model):

    def save(self, *args, **kwargs):
        normalize_txt(self)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True