from django.core.exceptions import ValidationError
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25, unique=True)
    parent = models.ForeignKey(
        to='self',
        on_delete=models.PROTECT,
        related_name='children',
        blank=True, null=True)
    icon = models.ImageField(upload_to='category/icons/%Y/%m/%d/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        try:
            if not self.pk and self.sub_categories.sub_categories.sub_categories:
                raise ValidationError('Subcategory cannot have more than 3 levels')
        except AttributeError:
            pass

    def __str__(self):
        return self.name