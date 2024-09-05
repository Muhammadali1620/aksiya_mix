from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class ServiceDiscount(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    icon = models.ImageField(upload_to='discount/icon/%Y/%m/%d')

    def __str__(self):
        return self.name


class Discount(models.Model):
    class Currency(models.IntegerChoices):
        UZS = 1, "UZS"
        USD = 2, "USD"

    class Status(models.IntegerChoices):
        CHECKING = 1, "CHECKING"
        ACCEPTED = 2, "ACCEPTED"
        REJECTED = 3, "REJECTED"
    
    class DiscountChoices(models.IntegerChoices):
        STANDARD = 1, 'STANDARD'
        FREE_PRODUCT = 2, 'FREE PRODUCT'
        QUANTITY_DISCOUNT = 3, 'QUANTITY DISCOUNT'
        SERVICE_DISCOUNT = 4, 'SERVICE DISCOUNT'

    _id = models.PositiveIntegerField(unique=True, primary_key=True, editable=False)

    company = models.ForeignKey("companies.Company", on_delete=models.CASCADE, related_name="discounts")
    filials = models.ManyToManyField("companies.Filial", related_name="discounts")
    category = models.ForeignKey("categories.Category", on_delete=models.PROTECT, related_name="discounts")

    discount_type = models.PositiveSmallIntegerField(choices=DiscountChoices.choices)
    
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1255, null=True, blank=True)
    video = models.FileField(upload_to='discount/video/%Y/%m/%d')

    available = models.PositiveIntegerField()

    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.PositiveSmallIntegerField(choices=Currency.choices, default=Currency.UZS)

    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.CHECKING)

    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    start_date = models.DateField()
    end_date = models.DateField()

    delivery = models.BooleanField(default=False)

    installment = models.BooleanField(default=False)

    #--standard discount--
    discount_value = models.DecimalField(max_digits=20, decimal_places=1, blank=True, null=True)
    discount_value_is_percent = models.BooleanField(default=False)

    #--free product discount--
    min_quantity = models.PositiveSmallIntegerField(blank=True, null=True)
    bonus_quantity = models.PositiveSmallIntegerField(blank=True, null=True)

    #--quantity discount--
    bonus_discount_value = models.DecimalField(max_digits=20, decimal_places=1, blank=True, null=True)
    bonus_discount_value_is_percent = models.BooleanField(default=False)

    #--service discount--
    service = models.ForeignKey(ServiceDiscount, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def clean(self):
        if self.discount_type == self.DiscountChoices.STANDARD:
            if self.discount_value is None:
                raise ValidationError("Discount value is required")
            
            if self.discount_value_is_percent and self.discount_value < 1 or self.discount_value > 100:
                raise ValidationError("Discount value must be between 1 and 100")
            
        if self.discount_type == self.DiscountChoices.FREE_PRODUCT:
            if self.min_quantity is None:
                raise ValidationError("Min quantity is required")
            
            if self.bonus_quantity is None:
                raise ValidationError("Bonus quantity is required")
            
        if self.discount_type == self.DiscountChoices.QUANTITY_DISCOUNT:
            if self.min_quantity is None:
                raise ValidationError("Min quantity is required")

            if self.bonus_discount_value is None:
                raise ValidationError("Bonus discount value is required")
            
            if self.bonus_discount_value_is_percent and self.bonus_discount_value < 1 or self.bonus_discount_value > 100:
                raise ValidationError("Bonus discount value must be between 1 and 100")

        if self.discount_type == self.DiscountChoices.SERVICE_DISCOUNT:
            if self.min_quantity is None:
                raise ValidationError("Min quantity is required")

            if self.service is None:
                raise ValidationError("Service is required")

        if self.start_date > self.end_date:
            raise ValidationError("Start date must be before end date")
        
        if self.end_date < timezone.now():
            raise ValidationError("End date must be in the future")


class DiscountImage(models.Model):
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='discount/image/%Y/%m/%d')
    ordering_number = models.PositiveIntegerField()