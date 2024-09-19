import random

from django.core.cache import cache
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError

from apps.authentication.services import generate_jwt_tokens
from apps.authentication.sms_providers import EskizUz
from apps.users.validators import phone_validate


class ForgotPasswordSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[phone_validate])
    link = serializers.CharField(read_only=True)

    def validate_username(self, phone_number):
        if not get_user_model().objects.filter(phone_number=phone_number).exists():
            raise ValidationError("User with this phone number does not exist.")
        return phone_number
    
    @classmethod
    def check_limit(cls, request):
        """
        Checking limit for ip address
        """
        ip_address = request.META.get('REMOTE_ADDR')

        limit = cache.get(ip_address, 0)
        if limit >= 3:
            raise exceptions.PermissionDenied('try after one hour')
        else:
            cache.set(ip_address, limit + 1, 60 * 60)

    def save(self, *args, **kwargs):
        """
        Send forgot password link to phone number user. 
        """
        # self.check_limit(self.context['request'])
        user = get_object_or_404(get_user_model(), phone_number=self.validated_data['username'])
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)

        reset_url =self.context['request'].build_absolute_uri(f'confirm/?token={token}')

        EskizUz.send_sms(
            send_type='FORGOT_PASSWORD', 
            phone_number=self.validated_data['username'],
            token=token,
            link=reset_url,
            )
        
        self.validated_data['link'] = reset_url


class NewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(validators=[validate_password], write_only=True)
    
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)

    def save(self, **kwargs):
        attrs = self.validated_data
        context = self.context

        token  = context['token']
        phone_number = cache.get(EskizUz.FORGOT_PASSWORD_KEY.format(token=token))
        
        if not phone_number:
            raise ValidationError('not found')
        
        user = get_object_or_404(get_user_model(), phone_number=phone_number)
        user.set_password(attrs['password'])
        user.save()

        cache.delete(EskizUz.FORGOT_PASSWORD_KEY.format(token=token))

        tokens = generate_jwt_tokens(user)

        self.validated_data['refresh'] = tokens['refresh']
        self.validated_data['access'] = tokens['access']


class SendCodeSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[phone_validate])

    def validate_username(self, phone_number):
        if get_user_model().objects.filter(phone_number=phone_number).exists():
            raise ValidationError("User with this phone number already exists.")
        return phone_number

    def save(self, *args, **kwargs):
        """
        Send registration code to phone number user.
        """
        # ForgotPasswordSerializer.check_limit(self.context['request'])

        code = EskizUz.send_sms(
            send_type='AUTH_CODE',
            phone_number=self.validated_data['username'],
            )

        self.validated_data['code'] = code


class VerifyCodeSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[phone_validate])
    code = serializers.IntegerField()

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number, code = attrs['username'], attrs['code']

        if cache.get(EskizUz.AUTH_CODE_KEY.format(phone_number=phone_number)) != code:
            raise serializers.ValidationError('Неверный номер телефона или код')

        return attrs
    

class RegisterSerializer(VerifyCodeSerializer):
    password = serializers.CharField(max_length=128, validators=[validate_password], write_only=True)
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number, password = attrs['username'], attrs['password']

        user = get_user_model().objects.create_user(phone_number=phone_number, password=password)

        cache.delete(EskizUz.AUTH_CODE_KEY.format(phone_number=phone_number))

        tokens = generate_jwt_tokens(user)

        attrs = {**attrs, **tokens}

        return attrs