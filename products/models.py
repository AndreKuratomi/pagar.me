from django.db import models
from django.utils import timezone

import uuid


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)

    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    seller = models.ForeignKey("accounts.User", null=True, on_delete=models.DO_NOTHING, related_name="products")


# Requisitos:
# Somente vendedores poderão cadastrar e atualizar seus próprios produtos.

# Não será possível a exclusão definitiva de produtos, ao invés disso, será feito um soft delete, 
# através do campo is_active, o vendedor poderá mudar o campo is_active através de uma atualização do produto. 
# Logo, não haverá uma rota de DELETE.
