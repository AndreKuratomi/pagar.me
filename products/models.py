from django.db import models

import uuid


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)

    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()
    is_active = models.BooleanField(default=True)

    seller = models.ForeignKey("accounts.User", on_delete=models.PROTECT, related_name="products")
