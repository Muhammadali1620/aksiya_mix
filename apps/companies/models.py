from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

from apps.categories.models import Category
from apps.users.validators import phone_validate


class Company(models.Model):
    _id = models.PositiveIntegerField(unique=True, primary_key=True, editable=False)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    logo = models.ImageField(upload_to='company/logo/%Y/%m/%d', blank=True, null=True)
    video = models.FileField(upload_to='company/videos/%Y/%m/%d', blank=True, null=True)
    banner = models.ImageField(upload_to='company/banner/%Y/%m/%d', blank=True, null=True)

    name = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=13, validators=[phone_validate])
    description = models.CharField(max_length=1255)

    followers = models.PositiveBigIntegerField(default=0)
    likes = models.PositiveBigIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    views = models.PositiveBigIntegerField(default=0)

    address = models.CharField(max_length=255)

    web_site = models.URLField()

    longitude = models.FloatField()
    latitude = models.FloatField()

    balance = models.DecimalField(max_digits=30, decimal_places=1, default=0)

    total_rating = models.FloatField(default=0, max_length=5, blank=True, null=True)
    rating5 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    rating4 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    rating3 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    rating2 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    rating1 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CompanyComment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    message = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)


class Filial(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    filial_number = models.CharField(max_length=13, validators=[phone_validate])
    address = models.CharField(max_length=255)

    longitude = models.FloatField()
    latitude = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CompanyTimeTable(models.Model):
    class WeekDays(models.IntegerChoices):
        SUNDAY = 0, 'SUNDAY'
        MONDAY = 1, 'MONDAY'
        TUESDAY = 2, 'TUESDAY'
        WEDNESDAY = 3, 'WEDNESDAY'
        THURSDAY = 4, 'THURSDAY'
        FRIDAY = 5, 'FRIDAY'
        SATURDAY = 6, 'SATURDAY'

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    week_day = models.PositiveSmallIntegerField(choices=WeekDays.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = (('company', 'week_day'),)

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError('Start time must be less than end time')