from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "first_name", "last_name", "is_admin", "is_seller"]

        extra_kwargs = {
            "password": {'write_only': True}
        }
