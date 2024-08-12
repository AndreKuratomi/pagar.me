from wsgiref import validate
from rest_framework import serializers

# from pagar_me_project.exceptions import InvalidCredentialsError
from accounts.models import User

import ipdb


class UserSerializer(serializers.ModelSerializer):
    class Meta: # why this class?
        model = User
        fields = ["id", "email", "password", "first_name", "last_name", "is_admin", "is_seller"]

        extra_kwargs = {
            "password": {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user
    

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "first_name", "last_name", "is_admin", "is_seller"]

        extra_kwargs = {
            "password": {'write_only': True}
        }


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
