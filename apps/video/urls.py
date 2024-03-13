from django.urls import path
from apps.video import views

urlpatterns = [
    path('video/<int:videoId>/', views.VideoDetailView.as_view()),
    path('video-mark/<int:videoId>/', views.VideoMark.as_view()),
    path('', views.VideoAppList.as_view()),
    path('moduls/', views.ModulsList.as_view()),
    path('create-comment/', views.CommentCreate.as_view()),
]
