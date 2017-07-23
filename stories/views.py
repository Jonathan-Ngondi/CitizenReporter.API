# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import (CreateAPIView, ListCreateAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateDestroyAPIView)

from stories.models import Media, Story
from stories.serializers import (MediaSerializer, StorySerializer,
                                 UserStoriesSerializer)


class UserStoriesView(RetrieveAPIView):
    serializer_class = UserStoriesSerializer
    lookup_field = 'fb_id'
    queryset = Story.objects.all()


class StoryCreateView(ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class StoriesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class MediaUploadView(CreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
