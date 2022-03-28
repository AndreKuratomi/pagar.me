from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.mixins import CreateModelMixin
from accounts.models import User

from products.models import Product
from products.serializers import ProductListSerializer, ProductSerializer
from products.permissions import IsSeller
from accounts.serializers import UserSerializer

import ipdb


class ProductView(ListCreateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductListSerializer
        return ProductSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSeller]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class ProductByIdView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSeller]

    lookup_url_kwarg = "product_id"


class ProductBySellerIdView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSeller]

    lookup_url_kwarg = "seller_id"
