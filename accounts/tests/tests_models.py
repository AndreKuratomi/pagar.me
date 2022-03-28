from django.test import TestCase

from user.models import User
from user.serializers import UserSerializer


class UserModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.email = "andre@mail.com"
        cls.password = "zxcvasdf"
        cls.first_name = "Andre"
        cls.last_name = "Kuratomi"
        cls.is_seller = True
        cls.is_admin = False

        cls.user = User.objects.create(
            email=cls.email,
            first_name=cls.first_name,
            last_name=cls.last_name,
            is_seller=cls.is_seller,
            is_admin=cls.is_admin
        )

    def test_user_fields(self):
        self.assertIsNot(self.user.is_seller, str)
        self.assertIsInstance(self.user.is_admin, bool)
        self.assertTrue(self.is_seller)

        # self.assertIn(self.last_name, )
        # self.assertNotIn(self.password, )

        self.assertEqual(self.user.first_name, self.first_name)
        self.assertIs(self.user.email, self.email)
