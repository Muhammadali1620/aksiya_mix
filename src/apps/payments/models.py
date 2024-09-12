from django.db import models
from django.core.validators import MinValueValidator

from apps.general.models import AbstractModel


class Payment(AbstractModel):
    company = models.ForeignKey('companies.Company',
                                 on_delete=models.SET_NULL,
                                 related_name='payments', 
                                 null=True)
    price = models.DecimalField(max_digits=30, decimal_places=2, validators=[MinValueValidator(0)])

    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return {self.price}