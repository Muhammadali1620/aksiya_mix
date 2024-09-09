from django.db import models
from django.core.cache import cache

from apps.discounts.choices import Currency


class CurrencyRate(models.Model):
    currency = models.PositiveSmallIntegerField(choices=Currency.choices, unique=True)
    in_sum = models.DecimalField(max_digits=20, decimal_places=3)

    def __str__(self):
        return f"{self.currency} - {self.in_sum}"