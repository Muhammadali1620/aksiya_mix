import os
import random

from django.core.cache import cache
from django.db.models import FileField, ImageField, CharField, TextField, SlugField
from django.template.defaultfilters import slugify

from apps.general.tasks import get_currency


def get_usd_in_sum():
    usd_in_sum = cache.get('usd_in_sum', None)
    if usd_in_sum is None:
        usd_in_sum = get_currency()
    return usd_in_sum


def normalize_txt(obj):
    for field  in obj._meta.get_fields():
        if isinstance(field, (CharField, TextField)):
            obj_field = getattr(obj, field.name)
            if not obj_field is None:
                setattr(obj, field.name, ' '.join(obj_field.split()))


def normalize_slug(obj):
    for field in obj._meta.get_fields():
        if isinstance(field, SlugField):
            obj_field = getattr(obj, field.name)
            if not obj_field is None:
                setattr(obj, field.name, slugify(obj_field))


def delete_file_after_delete_obj(instance):
    for field in instance._meta.get_fields():
        if isinstance(field, (FileField, ImageField)):
            file_field = getattr(instance, field.name)
            if file_field and os.path.isfile(file_field.path):
                os.remove(file_field.path)
            

def generate_id(instance):
    while True:
        _id = random.randint(100000, 999999)
        if not instance.objects.filter(_id=_id).exists():
            return str(_id)