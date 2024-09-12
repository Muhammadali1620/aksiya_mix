from django.conf import settings
from django.db import models

from apps.companies.models import Company
from apps.general.models import AbstractModel
from apps.users.validators import phone_validate


class Complaint(AbstractModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True)
    discount = models.ForeignKey('discounts.Discount', on_delete=models.SET_NULL, blank=True, null=True)

    message = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13, validators=[phone_validate])
    viewed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.phone_number:
            self.phone_number = self.user.phone_number
        super().save(*args, **kwargs)

    def clean(self):
        if not self.company or not self.discount:
            raise ValueError('Company and discount must be provided')

    def __str__(self):
        return self.phone_number