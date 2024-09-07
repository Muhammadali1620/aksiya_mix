from modeltranslation.translator import TranslationOptions, register

from apps.discounts.models import Discount, ServiceDiscount


@register(Discount)
class DiscountTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(ServiceDiscount)
class ServiceDiscountTranslationOptions(TranslationOptions):
    fields = ('name')