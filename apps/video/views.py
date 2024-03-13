from rest_framework.response import Response
from .models import VideoApp, ModulClass, Comment
from .serializer import VideoAppSerializer, ModulSerializer
from rest_framework.views import APIView
from rest_framework import status, permissions


class ModulsList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        candidates = ModulClass.objects.all()
        serializer = ModulSerializer(candidates, many=True)
        if serializer:
            response_data = {"moduls": serializer.data}
            return Response(response_data, status=status.HTTP_200_OK)

        return Response(
            {"error": "No Videos to list"},
            status=status.HTTP_404_NOT_FOUND)


class VideoAppList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        candidates = VideoApp.objects.all()
        serializer = VideoAppSerializer(candidates, many=True)
        if serializer:
            response_data = {"videos": serializer.data}
            return Response(response_data, status=status.HTTP_200_OK)

        return Response(
            {"error": "No Videos to list"},
            status=status.HTTP_404_NOT_FOUND)


class VideoDetailView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, videoId, format=None):
        try:
            video_id = int(videoId)
        except ValueError:
            return Response(
                {'error': 'Video ID must be an integer'},
                status=status.HTTP_400_BAD_REQUEST)

        video_marked = VideoApp.objects.get(id=video_id)
        first = VideoApp.objects.first()
        if video_marked == first:
            serializer = VideoAppSerializer(video_marked)
            return Response({'video': serializer.data}, status=status.HTTP_200_OK)
        else:
            all_videos = VideoApp.objects.all()
            filtered_videos = [video for video in all_videos
                               if video.id < video_marked.id and not video.marked_view]
            if len(filtered_videos) != 0:
                return Response({"data": "Video not access"})
            serializer = VideoAppSerializer(video_marked)
            return Response({'video': serializer.data}, status=status.HTTP_200_OK)


class VideoMark(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, videoId, format=None):
        video_id = int(videoId)
        video_marked = VideoApp.objects.get(id=video_id)
        if video_marked:
            video_marked.marked_view = True
            video_marked.save()
            return Response({"data": "Video marked as view"}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(
                {'error': 'Video ID must be an integer'},
                status=status.HTTP_400_BAD_REQUEST)


class CommentCreate(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        try:
            videoId = request.data.get('videoId')
            video_id = int(videoId)
            video_marked = VideoApp.objects.get(id=video_id)
            if video_marked:
                comment = Comment.objects.create(
                    commented_by=request.user, comment=request.data.get('body'))
                video_marked.comment.add(comment)
                video_marked.save()
                return Response({"data": "Created"}, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {'error': 'Video ID must be an integer'},
                    status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(
                {'error': 'Erorr'},
                status=status.HTTP_400_BAD_REQUEST)
