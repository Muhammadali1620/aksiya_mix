from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.DiscountCreateAPIView.as_view(), name='discount_create'),
    path('update/<int:pk>/', views.DiscountUpdateAPIView.as_view(), name='discount_update'),
    path('delete/<int:pk>/', views.DiscountDestroyAPIView.as_view(), name='discount_delete'),
    path('detail/<int:pk>/', views.DiscountRetrieveAPIView.as_view(), name='detail_delete'),
]