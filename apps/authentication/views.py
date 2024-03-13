from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from apps.authentication.serializers import LoginSerializer
from apps.users.models import User, Code
import random
from apps.general.authentication import get_user_auth_data


class LoginView(APIView):
    @staticmethod
    def generate_tokens(user):
        refresh = RefreshToken.for_user(user)
        access = AccessToken.for_user(user)
        return str(access), str(refresh)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        try:
            access_token, refresh_token = self.generate_tokens(user)
            code_ = Code.objects.get(user=user)
            code_default = random.randint(1000, 9999)
            code_.code = code_default
            code_.save()
            data = {
                'data': {'refresh': refresh_token, 'access': access_token},
                'user': get_user_auth_data(user, request)
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
