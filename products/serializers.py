from rest_framework import serializers
from accounts.serializers import UserSerializer

from products.models import Product

import ipdb


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

        extra_kwargs = {
            "quantity": {'min_value': 0}
        }

    seller = UserSerializer(read_only=True)


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

        extra_kwargs = {
            "seller": {'read_only': True}
        }
