from django.core.exceptions import ValidationError

from rest_framework import serializers

from apps.discounts.models import Discount



class DiscountCreateUpdateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        exclude = ('_id', 'status', 'views', 'likes', 'dislikes', 'comments',)

        def validate(self, data):
            many_to_many_fields = ['branches']
            m2m_data = {field: data.pop(field) for field in many_to_many_fields if field in data}

            model_instance = Discount(**data)

            try:
                model_instance.clean()
            except ValidationError as e:
                raise serializers.ValidationError(e.message_dict)
            
            data.update(m2m_data)
            
            return data


class DiscountRetrieveModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        exclude = ('dislikes', 'currency', 'in_stock', 'is_active', 'status', 'created_at', 'updated_at')