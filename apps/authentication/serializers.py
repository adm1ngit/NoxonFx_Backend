from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import User, Code


class LoginSerializer(serializers.Serializer):
    activate_code = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, attrs):
        try:
            code = Code.objects.get(code=attrs.get('activate_code'))
            usr = code.user
            user_ = usr.username
            pass_word_ = usr.pass_word
            user = authenticate(username=user_, password=pass_word_)
            user.save()
            if not user:
                raise serializers.ValidationError(
                    'Incorrect username or password.')

            if not user.is_active:
                raise serializers.ValidationError('User is deactivated.')

            return {'user': user}
        except:
            raise serializers.ValidationError(
                'Incorrect username or password.')


class TokenSerializer(serializers.Serializer):
    access_token = serializers.SerializerMethodField()
    refresh_token = serializers.SerializerMethodField()

    def create(self, validated_data):
        pass

    @staticmethod
    def get_access_token(user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    @staticmethod
    def get_refresh_token(user):
        refresh = RefreshToken.for_user(user)
        return str(refresh)

    def update(self, instance, validated_data):
        pass
