from django.forms import ValidationError
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from accounts.models import User
from pagar_me_project.exceptions import NotFoundSellerError

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
    print(serializer_class)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSeller]

    lookup_url_kwarg = "seller_id"

    def get(self, request, seller_id=''):
        try:
            seller = Product.objects.filter(seller=seller_id)

            if seller:
                serialized = ProductListSerializer(seller, many=True)
                return Response(serialized.data, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "This seller has no products yet!"}, status=status.HTTP_404_NOT_FOUND)

        except ValidationError:
            # return NotFoundSellerError
            return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_404_NOT_FOUND)