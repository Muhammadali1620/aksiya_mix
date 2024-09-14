from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from apps.discounts.models import Discount
from apps.discounts.serializers import DiscountCreateUpdateModelSerializer, DiscountRetrieveModelSerializer


class DiscountCreateAPIView(CreateAPIView):
    serializer_class = DiscountCreateUpdateModelSerializer


class DiscountUpdateAPIView(UpdateAPIView):
    serializer_class = DiscountCreateUpdateModelSerializer
    queryset = Discount.objects.all()


class DiscountDestroyAPIView(DestroyAPIView):
    queryset = Discount.objects.all()


class DiscountRetrieveAPIView(RetrieveAPIView):
    serializer_class = DiscountRetrieveModelSerializer
    queryset = Discount.objects.all()