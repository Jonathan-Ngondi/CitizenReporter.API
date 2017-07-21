# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics

from .serializers import ResponsesSerializer
from .models import Responses

class ResponsesList(generics.ListCreateAPIView):
    '''
    This class defines creation property of the api.
    '''
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializer

    def create_story(self, serializer):
        '''Saves posted stories.'''
        serializer.save()

class ResponsesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializer