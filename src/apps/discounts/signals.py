from django.dispatch import receiver
from django.db.models.signals import post_delete
from apps.general.services import delete_file_after_delete_obj
from apps.discounts.models import Discount, ServiceDiscount, DiscountImage


@receiver(post_delete, sender=Discount)
def delete_photo_on_delete_user(instance, *args, **kwargs):
    delete_file_after_delete_obj(instance)


@receiver(post_delete, sender=ServiceDiscount)
def delete_photo_on_delete_user(instance, *args, **kwargs):
    delete_file_after_delete_obj(instance)


@receiver(post_delete, sender=DiscountImage)
def delete_photo_on_delete_user(instance, *args, **kwargs):
    delete_file_after_delete_obj(instance)