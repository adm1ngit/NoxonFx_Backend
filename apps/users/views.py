from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.users.forms import SignUpForm
from apps.users.models import User, Code
from apps.users.serializers import CodeSerializer
import random


@api_view(['POST'])
def signup(request):
    data = request.data
    print(data)
    form = SignUpForm({
        'username': data.get('username'),
        'first_name': data.get('first_name'),
        'last_name': data.get('last_name'),
        'password1': data.get('password'),
        'password2': data.get('password')
    })

    if form.is_valid():
        user = form.save()
        user.pass_word = data.get('password')
        user.is_active = False
        user.save()
        return Response({"error": False}, status=status.HTTP_201_CREATED)
    else:
        return Response(
            {
                "error": True,
                "errors": form.errors,
            }, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
def activate_user(request):
    data = request.data
    try:
        user_id = data.get('username')
        user = User.objects.get(username=user_id)
        if user.is_active:
            if not Code.objects.filter(user=user).exists():
                code_default = random.randint(10000, 99999)
                code = Code.objects.create(user=user, code=code_default)
                code.save()
                serializer = CodeSerializer(code)
                return Response(serializer.data['code'], status=status.HTTP_200_OK)
            else:
                usr = User.objects.get(username=data.get('username'))
                code_ = Code.objects.get(user=usr)
                code_default = random.randint(10000, 99999)
                code_.code = code_default
                code_.save()
                serializer = CodeSerializer(code_)
                return Response(serializer.data['code'], status=status.HTTP_200_OK)
        else:
            return Response({"error": True, "data": 'foydalanuvchi topilmadi'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(
            {
                "error": True,
            }, status=status.HTTP_400_BAD_REQUEST
        )
