from django.contrib import admin
from django.conf import settings
from apps.users.models import User, Code

admin.site.register([User, Code,])
