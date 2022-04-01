from rest_framework.exceptions import APIException


class InvalidTokenError(APIException):
    status_code = '401'
    default_detail = {"detail": ["Invalid token."]}


class NotPermitedUserError(APIException):
    status_code = '403'
    default_detail = {"detail": ["You do not have permission to perform this action."]}


class NotFoundSellerError(APIException):
    status_code = '404'
    default_detail = {"detail": ["You do not have permission to perform this action."]}
