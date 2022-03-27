from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView

from django.contrib.auth import authenticate

from fees.models import Fee
from fees.serializers import FeeSerializer
from fees.permissions import IsAdmin

import ipdb


class FeeView(ListCreateAPIView):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdmin]


class FeeByIdView(ListCreateAPIView):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdmin]

    lookup_url_kwarg = "fee_id"
