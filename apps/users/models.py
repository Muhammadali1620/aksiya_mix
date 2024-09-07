from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.users.managers import CustomUserManager
from apps.users.validators import phone_validate


class CustomUser(AbstractUser):
    class Gender(models.IntegerChoices):
        MAN = 1, 'Мужчина'
        WOMAN = 2, 'Женщина'

    USERNAME_FIELD = 'phone_number'
    username = None
    objects = CustomUserManager()
    
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    phone_number = models.CharField(max_length=13, unique=True, validators=[phone_validate])
    email = models.EmailField(unique=True, blank=True, null=True)
    
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.PositiveSmallIntegerField(choices=Gender.choices, blank=True, null=True)
    
    address = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.phone_number