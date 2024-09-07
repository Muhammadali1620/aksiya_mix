from django.conf import settings
from django.db import models

from apps.companies.models import Company
from apps.users.validators import phone_validate


class Complaint(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

    message = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13, validators=[phone_validate], blank=True, null=True)
    viewed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.phone_number is None or self.phone_number == '':
            self.phone_number = self.user.phone_number
        super().save(*args, **kwargs)

    def __str__(self):
        return self.phone_number