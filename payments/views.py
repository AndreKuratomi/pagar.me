from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import CreateModelMixin

from payments.models import Payment
from payments.serializers import PaymentSerializer
from payments.permissions import IsBuyer

import ipdb


class PaymentView(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsBuyer]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
