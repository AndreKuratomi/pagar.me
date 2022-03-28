from django.db import models
from django.utils import timezone

import uuid


class Fee(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)

    credit_fee = models.CharField(max_length=5, unique=True)
    debit_fee = models.CharField(max_length=5, unique=True)

    created_at = models.DateTimeField(default=timezone.now)


# Deverão existir as seguintes taxas padrões no sistema:
# Cartão de crédito - 5%
# Cartão de débito - 3%
# Não deve ser possível a exclusão de taxas no sistema.
