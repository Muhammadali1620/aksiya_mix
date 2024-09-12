from modeltranslation.translator import TranslationOptions, register

from apps.features.models import Feature, FeatureValue


@register(FeatureValue)
class FeatureValueTranslationOptions(TranslationOptions):
    fields = ('value',)


@register(Feature)
class FeatureTranslationOptions(TranslationOptions):
    fields = ('name',)