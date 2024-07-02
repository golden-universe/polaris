from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from account.v2.serializers import UserLoginSerializer, UserSerializer
from services.auth import CacheSession


class UserLoginAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        token = CacheSession().add(request=request, user=user)

        user_detail_serializer = UserSerializer(user)
        return Response(user_detail_serializer.data | {"token": token}, status=HTTP_200_OK)


class UserLogoutAPIView(CreateAPIView):
    authentication_classes = [SessionAuthentication]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        request.session.delete()
        return Response(status=HTTP_200_OK)
