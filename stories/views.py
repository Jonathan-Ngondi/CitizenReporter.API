# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import (CreateAPIView, ListCreateAPIView,
                                     ListAPIView,
                                     RetrieveUpdateDestroyAPIView)

from stories.models import Media, Story
from stories.serializers import (MediaSerializer, StorySerializer,
                                 UserStoriesSerializer)


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


class StoriesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class MediaUploadView(CreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
