# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import (CreateAPIView, ListCreateAPIView,
                                     ListAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from stories.models import Media, Story
from stories.serializers import (MediaSerializer, StorySerializer,
                                 UserStoriesSerializer, ParseStorySerializer)


class UserStoriesView(ListAPIView):
    serializer_class = UserStoriesSerializer
    lookup_field = 'fb_id'

    def get_queryset(self):
        """
        This view should return a list of all the stories for
        the user as determined by the fb_id portion of the URL.
        """
        fb_id = self.kwargs['fb_id']
        return Story.objects.filter(fb_id=fb_id)


class StoryCreateView(ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    
class ParseStoryCreateView(APIView):
    def post(self, request, format=None):
      
        data = request.data["object"]
        data["when"] = data["when"]["iso"]
        data["local_id"] = data["localID"]
        data["assignmentId"] = data["assignment"]
        data["where"] = data["location"]
        data["updated"] = data["updatedAt"]
        data["created"] = data["createdAt"]
        data["local_media_paths"] = [f["url"] for f in data["media"]]
        
        del data["localID"], data["assignment"], data["media"],
        data["className"], data["location"], data["updatedAt"], data["createdAt"]
        serializer = ParseStorySerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # serializer = ParseStorySerializer(data=req)


class StoriesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class MediaUploadView(CreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
