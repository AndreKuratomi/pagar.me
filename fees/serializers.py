from rest_framework import serializers

# from pagar_me.exceptions import InvalidCredentialsError
from fees.models import Fee


class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = "__all__"
