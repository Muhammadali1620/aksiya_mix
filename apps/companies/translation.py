from modeltranslation.translator import TranslationOptions, register

from apps.companies.models import Company, Filial


@register(Company)
class CompanyTranslationOptions(TranslationOptions):
    fields = ('description', 'address', 'slogan')


@register(Filial)
class FilialTranslationOptions(TranslationOptions):
    fields = ('address')