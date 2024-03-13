from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from apps.authentication.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('refresh/', TokenRefreshView.as_view())
]
