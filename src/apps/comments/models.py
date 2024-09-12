from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

from apps.discounts.models import Discount
from apps.general.models import AbstractModel
from apps.users.validators import phone_validate


class Comment(AbstractModel):
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey(to='self',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)

    phone_number = models.CharField(max_length=13, validators=[phone_validate])
    message = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.phone_number:
            self.phone_number = self.user.phone_number
        super().save(*args, **kwargs)

        try:
            if not self.pk and self.parent.parent:
                raise ValidationError('You cannot reply to a reply')
        except AttributeError:
            pass

    def __str__(self):
        return self.phone_number