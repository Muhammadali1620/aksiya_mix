import requests
from celery import shared_task

from apps.general.models import CurrencyRate, Currency


@shared_task
def get_currency():
    response = requests.get('https://cbu.uz/oz/arkhiv-kursov-valyut/json/')
    obj = CurrencyRate.objects.filter(currency=Currency.USD).first()
    if obj:
        obj.in_sum = response.json()[0]['Rate']
        obj.save()
    else:
        CurrencyRate.objects.create(currency=Currency.USD, in_sum=response.json()[0]['Rate'])
    print(response.json()[0]['Rate'])