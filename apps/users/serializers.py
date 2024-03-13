from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from apps.users.models import Code

User = get_user_model()


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('avatar', 'name',
                  'number', 'address', 'id', 'username',)


class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('avatar',)


class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'username',]


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ['code',]
