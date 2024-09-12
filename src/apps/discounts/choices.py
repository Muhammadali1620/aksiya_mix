from django.db import models


class Currency(models.IntegerChoices):
    UZS = 1, "UZS"
    USD = 2, "USD"