from django.db import models
from django.conf import settings

from apps.discounts.models import Discount



class DiscountComment(models.Model):
    company = models.ForeignKey(Discount, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    message = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message