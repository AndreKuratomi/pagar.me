from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView

from products.models import Product
from products.serializers import ProductSerializer
from products.permissions import IsSeller

import ipdb


class ProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsSeller]


class ProductByIdView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSeller]

    lookup_url_kwarg = "product_id"


class ProductBySellerIdView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSeller]

    lookup_url_kwarg = "seller_id"
