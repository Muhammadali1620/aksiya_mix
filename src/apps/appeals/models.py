from django.conf import settings
from django.db import models

from apps.general.models import AbstractModel


class Appeal(AbstractModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=13)
    
    message = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.phone_number:
            self.phone_number = self.user.phone_number
        super().save(*args, **kwargs)

    def __str__(self):
        return self.phone_number