import requests

from django.core.cache import cache
from celery import shared_task



@shared_task
def get_currency():
    response = requests.get('https://cbu.uz/oz/arkhiv-kursov-valyut/json/')
    usd_in_sum = response.json()[0]['Rate']
    cache.set('usd_in_sum', usd_in_sum, timeout=60 * 60 * 24)
    return usd_in_sum