from rest_framework import serializers

from pagar_me.exceptions import NegativeQuantityError
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "description", "quantity", "is_active", "seller"]

        def validate(self, attrs):
            quantity = attrs['quantity']
            print(quantity)

            is_quantity_not_positive = Product.objects.filter(quantity=quantity).exists()
            print(is_quantity_not_positive)
            if is_quantity_not_positive < 0:
                raise NegativeQuantityError

            return super().validate(attrs)
