from rest_framework import serializers
from .models import VideoApp, ModulClass, Comment
from apps.users.serializers import UserReadSerializer


class CommentSerializer(serializers.ModelSerializer):
    created_by = UserReadSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'created_by', 'comment',)


class VideoAppSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True)

    class Meta:
        model = VideoApp
        fields = ('id', 'name', 'video', 'description',
                  'comment', 'created_at', 'marked_view')


class ModulSerializer(serializers.ModelSerializer):
    videos = VideoAppSerializer(
        source='videoapp_set', many=True, read_only=True)

    class Meta:
        model = ModulClass
        fields = ('id', 'name', 'videos', 'created_at')
