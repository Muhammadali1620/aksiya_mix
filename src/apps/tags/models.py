from django.db import models

from apps.general.models import AbstractModel


class Tags(AbstractModel):
    name = models.SlugField(max_length=25, unique=True)

    def __str__(self):
        return self.name