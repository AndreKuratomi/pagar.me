from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView

from user.models import User
from user.serializers import UserSerializer
from user.permissions import isAdmin


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdmin]
