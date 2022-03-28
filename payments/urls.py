from django.urls import path
from payments.views import PaymentView

urlpatterns = [
    path('payment_info/', PaymentView.as_view())
]
