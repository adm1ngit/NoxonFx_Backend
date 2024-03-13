from django.contrib.auth.forms import UserCreationForm
from apps.users.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'password1', 'password2',)
