from django.db import models

from apps.categories.models import Category
from apps.discounts.models import Discount


class Advertisement(models.Model):
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True, null=True)

    start_date = models.DateField()
    end_date = models.DateField()

    image = models.ImageField(upload_to='advertisement/image/%Y/%m/%d')

    old_price = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    sale_price = models.DecimalField(max_digits=10, decimal_places=1, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title