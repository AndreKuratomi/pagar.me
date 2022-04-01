from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import CreateModelMixin

from payments.models import PaymentInfo
from payments.serializers import PaymentSerializer
from payments.permissions import IsBuyer

import ipdb


class PaymentView(ListCreateAPIView):
    queryset = PaymentInfo.objects.all()
    serializer_class = PaymentSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsBuyer]

    def get_queryset(self):
        queryset = PaymentInfo.objects.filter(customer=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
