from typing import Iterable
from django.conf import settings
from django.db import models


class Appeal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=13, blank=True)
    
    message = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number
    
    def save(self, *args, **kwargs):
        if self.phone_number is None or self.phone_number == '':
            self.phone_number = self.user.phone_number
        super().save(*args, **kwargs)