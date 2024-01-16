from django.contrib.auth.views import get_user_model
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer

User = get_user_model()


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        confirm_password = request.data['confirm_password']
        data = request.data

        if password != confirm_password:
            return Response({'message': 'Password aro not same!'})
        if User.objects.filter(username=username).exists():
            return Response({'message': 'Username already exists! '})

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        refresh_token = request.data.get
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=204)
