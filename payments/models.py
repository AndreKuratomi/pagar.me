from django.db import models

import uuid


class PaymentInfo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)

    payment_method = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
    cardholders_name = models.CharField(max_length=255)
    card_expiring_date = models.CharField(max_length=255)
    cvv = models.IntegerField()
    is_active = models.BooleanField(default=True)

    customer = models.ForeignKey("accounts.User", on_delete=models.PROTECT, related_name="payments_infos")
