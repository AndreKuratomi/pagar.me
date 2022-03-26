from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone

import uuid


class CustomUserManager(BaseUserManager):

    def _create_user(
        self,
        email,
        password,
        is_staff,
        is_superuser,
        **extra_fields
    ):
        now = timezone.now()

        if not email:
            raise ValueError('The given email must be set!')

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)

    email = models.EmailField(editable=True, max_length=255, unique=True)
    password = models.CharField(max_length=255)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True, unique=False)

    is_admin = models.BooleanField()
    is_seller = models.BooleanField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


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