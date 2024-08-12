from django.utils import timezone

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
        now = timezone.now().date()

        # lt = less than
        PaymentInfo.objects.filter(card_expiring_date__lt=now, is_active=True).update(is_active=False)

        queryset = PaymentInfo.objects.filter(customer=self.request.user)
        return queryset

    # ipdb.set_trace()
    # def perform_create(self, serializer):
    #     print("asdf", serializer)
    #     serializer.save(customer=self.request.user)

    # def get_serializer_class(self):
    #     if self.request.method == "GET":
    #         return ProductListSerializer
    #     return ProductSerializer
