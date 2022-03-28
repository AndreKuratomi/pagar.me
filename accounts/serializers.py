from rest_framework import serializers

# from pagar_me.exceptions import InvalidCredentialsError
from accounts.models import User

import ipdb


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "first_name", "last_name", "is_admin", "is_seller"]

        extra_kwargs = {
            "password": {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'], first_name=validated_data['first_name'], last_name=validated_data['last_name'], is_seller=validated_data['is_seller'], is_admin=validated_data['is_admin'])

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

# class LoginUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Login
#         fields = "__all__"

#         def validate(self, attrs):

#             email = attrs['email']

#             does_email_exist = User.objects.filter(email=email).exists()
#             if not does_email_exist:
#                 raise InvalidCredentialsError

#             password = attrs['password']

#             does_password_exist = User.objects.filter(password=password).exists()
#             if not does_password_exist:
#                 raise InvalidCredentialsError
# #           ???
#             user = authenticate(email=email, password=password)
#             if user is not None:
#                 token = Token.objects.get_or_create(user=user)[0]
#                 return {'token': token.key}

#             return super().validate(attrs)
