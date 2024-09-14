from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.core.validators import MinValueValidator

from apps.categories.models import Category
from apps.companies.region_choices import Regions , District
from apps.companies.validators import validate_company_video_size, validate_company_logo_size, validate_company_banner_size, validate_image_size
from apps.general.models import AbstractModel
from apps.general.services import generate_id
from apps.users.validators import phone_validate


class Company(AbstractModel):
    _id = models.CharField(unique=True, editable=False)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    categories = models.ManyToManyField(Category, blank=True)

    logo = models.ImageField(upload_to='company/logo/%Y/%m/%d/', 
                             blank=True, 
                             null=True,
                             validators=[validate_company_logo_size])
    video = models.FileField(upload_to='company/videos/%Y/%m/%d/', 
                             blank=True, 
                             null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['mp4']),
                                         validate_company_video_size])
    banner = models.ImageField(upload_to='company/banner/%Y/%m/%d/', 
                               blank=True, 
                               null=True,
                               validators=[validate_company_banner_size,
                                           validate_image_size])

    name = models.CharField(max_length=150)
    username = models.SlugField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=13, validators=[phone_validate])
    description = models.TextField(max_length=1000)

    followers = models.CharField(max_length=40, default='0')
    likes = models.CharField(max_length=40, default='0')
    comments = models.CharField(max_length=50, default='0')
    views = models.CharField(max_length=50, default='0')

    installment = models.BooleanField(default=False)

    web_site = models.URLField(blank=True, null=True)

    slogan = models.CharField(max_length=30, blank=True, null=True)

    region = models.PositiveSmallIntegerField(choices=Regions.choices)
    district = models.CharField(choices=District.choices)
    address = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()

    balance = models.DecimalField(max_digits=30, 
                                  decimal_places=1, 
                                  default=0,
                                  validators=[MinValueValidator(0)])

    rating1 = models.CharField(max_length=50, default='0')
    rating2 = models.CharField(max_length=50, default='0')
    rating3 = models.CharField(max_length=50, default='0')
    rating4 = models.CharField(max_length=50, default='0')
    rating5 = models.CharField(max_length=50, default='0')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_address(self):
        return {
            'region': self.region,
            'district': self.district,
            'address': self.address,
            'longitude': self.longitude,
            'latitude': self.latitude,
        }

    def clean(self):
        if self.district and self.district.split('X')[0] != str(self.region):
            raise ValidationError({'region':'District and region do not match'})
        
    def save(self, *args, **kwargs):
        self._id = generate_id(Company)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.username


class Filial(AbstractModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, validators=[phone_validate])

    delivery = models.BooleanField(default=False)

    region = models.PositiveSmallIntegerField(choices=Regions.choices)
    district = models.PositiveSmallIntegerField(choices=District.choices)
    address = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def get_address(self):
        return {
            'region': self.region,
            'district': self.district,
            'address': self.address,
            'longitude': self.longitude,
            'latitude': self.latitude,
        }

    def __str__(self):
        return self.name


class CompanyTimeTable(AbstractModel):
    class WeekDays(models.IntegerChoices):
        SUNDAY = 0, 'SUNDAY'
        MONDAY = 1, 'MONDAY'
        TUESDAY = 2, 'TUESDAY'
        WEDNESDAY = 3, 'WEDNESDAY'
        THURSDAY = 4, 'THURSDAY'
        FRIDAY = 5, 'FRIDAY'
        SATURDAY = 6, 'SATURDAY'

    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE, blank=True, null=True)


    week_day = models.PositiveSmallIntegerField(choices=WeekDays.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = (('company', 'week_day'),
                           ('filial', 'week_day'))

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError({'start_time':'Start time must be less than end time'})
        
        if self.company and self.filial:
            raise ValidationError({'Company and Filial cannot be set together'})