from django.contrib.auth.models import BaseUserManager
from django.db import transaction, models
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):

    def create_superuser(self, username, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, **extra_fields)

    @transaction.atomic
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')

        user = self.model(username=username, password=None, **extra_fields)
        user.pass_word = password
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractUser):
    pass_word = models.CharField(max_length=300, null=True, blank=True)
    number = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    img = models.ImageField(upload_to='avatars', blank=True, null=True)

    def name(self):
        if self.first_name and self.last_login:
            return f"{self.first_name} {self.last_login}"
        else:
            return f"{self.first_name}"

    def avatar(self):
        if self.img:
            return str(self.img.url)
        else:
            return 'https://picsum.photos/200/200'

    objects = UserManager()

    class Meta:
        verbose_name = 'Telegram user'
        verbose_name_plural = 'Telegram users'


class Code(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.SmallIntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return str(f"{self.user} - {self.code}")

    class Meta:
        verbose_name = 'User code'
        verbose_name_plural = 'Users login code'
