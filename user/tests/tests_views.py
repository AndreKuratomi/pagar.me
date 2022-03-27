from rest_framework.test import APITestCase

from user.models import User


class UserViewTests(APITestCase):

    def test_create_fail_case1(self):
        user_data = {
            "password": "zxcvasdf",
            "first_name": "Andre",
            "last_name": "Kuratomi",
            "is_seller": True,
            "is_admin": False
        }

        response = self.client.post('/api/accounts/', user_data)

        self.assertEqual(response.status_code, 400)
        self.assertNotEqual(response.status_code, 200)

        self.assertIn("email", response.json())

    def test_create_sucess(self):
        user_data = {
            "email": "andre@mail.com",
            "password": "zxcvasdf",
            "first_name": "Andre",
            "last_name": "Kuratomi",
            "is_seller": True,
            "is_admin": False
        }

        response = self.client.post('/api/accounts/', user_data)

        self.assertIs(response.status_code, 201)
        self.assertNotEqual(response.status_code, 200)

        self.assertIn('id', response.json())
        self.assertNotIn('password', response.json())

    def test_create_fail_case2(self):
        user_data = {
            "email": "andre@mail.com",
            "password": "zxcvasdf",
            "first_name": "Andre",
            "last_name": "Kuratomi",
            "is_seller": True,
            "is_admin": False
        }

        response = self.client.post('/api/accounts/', user_data)

        user_data_repeated = {
            "email": "andre@mail.com",
            "password": "zxcvasdf",
            "first_name": "Andre",
            "last_name": "Kuratomi",
            "is_seller": True,
            "is_admin": False
        }

        response = self.client.post('/api/accounts/', user_data_repeated)

        self.assertEqual(response.status_code, 400)
        self.assertIn('email', response.json())


# class LoginUserViewTest(APITestCase):
#     def setUp(self) -> None:
#         User.objects.create_user(
#             email="andre@mail.com",
#             password="zxcvasdf"
#         )

#     def test_login_success(self):
#         login_data = {
#             "email": "andre@mail.com",
#             "password": "zxcvasdf"
#         }

#         response = self.client.post('/api/login/', login_data)

#         self.assertEqual(response.status_code, 200)
#         self.assertIn('token', response.json())

#     def test_login_invalid_credentials1(self):
#         login_data = {
#             "email": "richarson@notmail.com",
#             "password": "qwerty"
#         }

#         response = self.client.post('/api/login/', login_data)

#         self.assertEqual(response.status_code, 401)

#     def test_login_invalid_credentials2(self):
#         login_data = {
#             "email": "andre@mail.com",

#         }

#         response = self.client.post('/api/login/', login_data)

#         self.assertEqual(response.status_code, 401)
