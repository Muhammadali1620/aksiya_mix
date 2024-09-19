from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.authentication import views


urlpatterns = [
    # ========== Jwt Authentication ========== #
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ========== Register ========== #
    path('register/send_code/', views.SendCodeAPIView.as_view(), name='send_code'),
    path('register/verify_code/', views.VerifyCodeAPIView.as_view(), name='verify_code'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),

    # ========== Forgot Password ========== #
    path('forgot_password/', views.ForgotPasswordAPIView.as_view(), name='forgot_password'),
    path('forgot_password/confirm/', views.NewPasswordAPIView.as_view(), name='new_password'),
]