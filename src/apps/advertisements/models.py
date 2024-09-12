from django.db import models
from django.core.validators import MinValueValidator

from apps.companies.validators import validate_company_banner_size, validate_image_size
from apps.general.models import AbstractModel


class Advertisement(AbstractModel):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    image = models.ImageField(upload_to='advertisement/image/%Y/%m/%d/', 
                              validators=[validate_company_banner_size,
                                          validate_image_size])

    old_price = models.DecimalField(max_digits=10,
                                    decimal_places=1,
                                    default=0,
                                    validators=[MinValueValidator(0)])
    sale_price = models.DecimalField(max_digits=10, 
                                     decimal_places=1, 
                                     default=0,
                                     validators=[MinValueValidator(0)])

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title