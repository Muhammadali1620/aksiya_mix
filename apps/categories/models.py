from django.core.exceptions import ValidationError
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25, unique=True)
    sub_categories = models.ForeignKey('self', on_delete=models.PROTECT, related_name='categories')
    description = models.CharField(max_length=300)
    icon = models.ImageField(upload_to='category/icons/%Y/%m/%d')

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.pk and self.sub_categories:
            if self.sub_categories.sub_categories:
                if self.sub_categories.sub_categories.sub_categories:
                    raise ValidationError('Subcategory cannot have more than 3 levels')

    def __str__(self):
        return self.name