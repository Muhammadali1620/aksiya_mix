from django.core.cache import cache

from apps.discounts.choices import Currency
from apps.general.tasks import get_currency
from apps.general.models import CurrencyRate


def get_usd_in_sum():
    usd_in_sum = cache.get('usd_in_sum', None)
    if usd_in_sum is None:
        obj = CurrencyRate.objects.filter(currency=Currency.USD).first()
        if obj:
            usd_in_sum = obj.in_sum
        else:
            usd_in_sum = get_currency().in_sum
        cache.set('usd_in_sum', usd_in_sum, timeout=60 * 60 * 24)
    return usd_in_sum