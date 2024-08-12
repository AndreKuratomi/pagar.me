
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from django.contrib.auth import authenticate

from accounts.models import User
from accounts.serializers import LoginSerializer, UserListSerializer, UserSerializer
from accounts.permissions import IsAdmin

import ipdb


class LoginUserView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        print(serializer)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])

        if user is not None:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({'token': token.key})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]


class UserByIdView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    authentication_classes = [TokenAuthentication]
    # permission_class = [] ? only the own user may update its data

    lookup_url_kwarg = "user_id"

    # and how to only inactivate a user? is_active as permission to login and update ist own data
