from apps.authentication.serializers import TokenSerializer
from apps.users.serializers import UserReadSerializer


def get_user_auth_data(user, request):
    return UserReadSerializer(user).data
