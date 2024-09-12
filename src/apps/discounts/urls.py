from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.DiscountCreateAPIView.as_view(), name='discount_create'),
]