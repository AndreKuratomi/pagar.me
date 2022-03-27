from rest_framework.exceptions import APIException


class InvalidCredentialsError(APIException):
    status_code = '401'
    default_detail = {"message": ["Invalid credentials"]}
