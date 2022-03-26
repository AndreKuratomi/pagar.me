from django.db import models


class User(models.Model):
    id = models.UUIDField(editable=False, unique=True)
    email = models.EmailField(editable=True, unique=True)
    password = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    is_admin = models.BooleanField()
    is_seller = models.BooleanField()

# Sobre Usuários (User):
# A aplicação terá 3 tipos de usuário:

# Administrador - is_seller=False, is_admin=True

# Vendedor - is_seller=True, is_admin=False

# Comprador - is_seller=False, is_admin=False

# Requisitos:
# O id deverá ser do tipo uuid.
# O campo de identificação exclusivo do usuário será o e-mail.
# Somente administradores poderão visualizar a lista de usuários no sistema.
# A criação dos usuários não deverá ter nenhum tipo de autenticação.
# O campo de password não deve ser retornado para o usuário.
# Tratamentos de Erros:
# Caso seja feita a tentativa de algum usuário cujo e-mail já esteja cadastrado no sistema, a resposta deverá ser:
# STATUS 400 - {"email": ["user with this email already exists."]}