from rest_framework import serializers
from apps.discounts.models import Discount


class DiscountCreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        exclude = ('_id', 'status', 'views', 'likes', 'dislikes', 'comments',)