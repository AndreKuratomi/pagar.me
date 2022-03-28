from rest_framework.permissions import BasePermission


class IsBuyer(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user.is_authenticated and not
                    request.user.is_seller and not
                    request.user.is_admin)
