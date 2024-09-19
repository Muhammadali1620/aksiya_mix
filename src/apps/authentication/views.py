from django.core.cache import cache

from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView

from apps.authentication.serializers import (ForgotPasswordSerializer, RegisterSerializer, SendCodeSerializer,
                                              VerifyCodeSerializer, NewPasswordSerializer)
from apps.authentication.sms_providers import EskizUz


class ForgotPasswordAPIView(CreateAPIView):
    """
    This view is send link to phone number.
    """
    permission_classes = ()
    authentication_classes = ()

    serializer_class = ForgotPasswordSerializer


class NewPasswordAPIView(GenericAPIView):
    """
    This view is set new password to user.
    """
    queryset = []

    permission_classes = ()
    authentication_classes = ()

    serializer_class = NewPasswordSerializer

    def get(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        token_in_cache = cache.get(EskizUz.FORGOT_PASSWORD_KEY.format(token=token))
        if not token_in_cache:
            return Response({'error': 'request not found'}, status=404)
        return Response(status=200)

    def post(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        serializer = self.get_serializer(data=request.data, 
                                         context={'token':token,})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class SendCodeAPIView(GenericAPIView):
    """
    This view is send verification code to the phone number.
    """
    permission_classes = ()
    authentication_classes = ()

    serializer_class = SendCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         context={'request': request,})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=200)
    

class VerifyCodeAPIView(GenericAPIView):
    """
    This view is check verify code 
    """
    permission_classes = ()
    authentication_classes = ()

    serializer_class = VerifyCodeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)
    

class RegisterAPIView(GenericAPIView):
    """
    This view is register a new user.
    """
    permission_classes = ()
    authentication_classes = ()

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)