from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.core.validators import MinValueValidator

from apps.companies.validators import validate_company_video_size
from apps.discounts.choices import Currency
from apps.general.models import AbstractModel
from apps.general.services import generate_id, get_usd_in_sum


class ServiceDiscount(AbstractModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    icon = models.ImageField(upload_to='discount/icon/%Y/%m/%d/', blank=True, null=True)

    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Discount(AbstractModel):
    class Status(models.IntegerChoices):
        PROCESS = 1, "PROCESS"
        ACCEPTED = 2, "ACCEPTED"
        REJECTED = 3, "REJECTED"
    
    class Types(models.IntegerChoices):
        STANDARD = 1, 'STANDARD'
        FREE_PRODUCT = 2, 'FREE PRODUCT'
        QUANTITY_DISCOUNT = 3, 'QUANTITY DISCOUNT'
        SERVICE_DISCOUNT = 4, 'SERVICE DISCOUNT'

    _id = models.PositiveIntegerField(unique=True, editable=False)

    company = models.ForeignKey("companies.Company", on_delete=models.CASCADE, related_name="discounts")
    branches = models.ManyToManyField("companies.Filial", 
                                      related_name="discounts", 
                                      blank=True)
    category = models.ForeignKey("categories.Category", 
                                 on_delete=models.PROTECT, 
                                 related_name="discounts",
                                 limit_choices_to={'parent__parent__isnull: False'})

    discount_type = models.PositiveSmallIntegerField(choices=Types.choices)
    
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    video = models.FileField(upload_to='discount/video/%Y/%m/%d/',
                             blank=True,
                             null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['mp4']),
                                         validate_company_video_size])

    available = models.PositiveIntegerField()

    old_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    currency = models.PositiveSmallIntegerField(choices=Currency.choices, default=Currency.UZS)

    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.PROCESS)

    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)

    start_date = models.DateField()
    end_date = models.DateField()

    delivery = models.BooleanField(default=False)

    installment = models.BooleanField(default=False)

    #--standard discount--
    discount_value = models.DecimalField(max_digits=20,
                                         decimal_places=1, 
                                         blank=True, 
                                         null=True,
                                         validators=[MinValueValidator(0)])
    discount_value_is_percent = models.BooleanField(default=False)

    #--free product discount--
    min_quantity = models.PositiveSmallIntegerField(blank=True, null=True)
    bonus_quantity = models.PositiveSmallIntegerField(blank=True, null=True)

    #--quantity discount--
    bonus_discount_value = models.DecimalField(max_digits=20, 
                                               decimal_places=1, 
                                               blank=True, 
                                               null=True,
                                               validators=[MinValueValidator(0)])
    bonus_discount_value_is_percent = models.BooleanField(default=False)

    #--service discount--
    service = models.ForeignKey(ServiceDiscount, on_delete=models.SET_NULL, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_old_price_by_currency(self, currency):
        if currency != self.currency:
            usd_in_sum = get_usd_in_sum()
            return usd_in_sum * self.old_price
        return self.old_price           
        
    def clean(self):
        if self.discount_type == self.Types.STANDARD:
            if self.discount_value is None:
                raise ValidationError("Discount value is required")
            
            if self.discount_value_is_percent and self.discount_value < 1 or self.discount_value > 100:
                raise ValidationError("Discount value must be between 1 and 100")
            
        if self.discount_type == self.Types.FREE_PRODUCT:
            if self.min_quantity is None:
                raise ValidationError("Min quantity is required")
            
            if self.bonus_quantity is None:
                raise ValidationError("Bonus quantity is required")
            
        if self.discount_type == self.Types.QUANTITY_DISCOUNT:
            if self.min_quantity is None:
                raise ValidationError("Min quantity is required")

            if self.bonus_discount_value is None:
                raise ValidationError("Bonus discount value is required")
            
            if self.bonus_discount_value_is_percent and self.bonus_discount_value < 1 or self.bonus_discount_value > 100:
                raise ValidationError("Bonus discount value must be between 1 and 100")

        if self.discount_type == self.Types.SERVICE_DISCOUNT:
            if self.min_quantity is None:
                raise ValidationError("Min quantity is required")

            if self.service is None:
                raise ValidationError("Service is required")

        if self.start_date > self.end_date:
            raise ValidationError("Start date must be before end date")
        
        if self.end_date < timezone.now():
            raise ValidationError("End date must be in the future")

    def save(self, *args, **kwargs):
        self._id = generate_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class DiscountImage(AbstractModel):
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='discount/image/%Y/%m/%d/')
    ordering_number = models.PositiveIntegerField()