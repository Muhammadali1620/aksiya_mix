from rest_framework.generics import CreateAPIView

from apps.discounts.serializers import DiscountCreateModelSerializer


class DiscountCreateAPIView(CreateAPIView):
    serializer_class = DiscountCreateModelSerializer
