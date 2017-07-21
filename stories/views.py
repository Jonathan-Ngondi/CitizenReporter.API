# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics

from .serializers import ResponsesSerializer, UserStoriesSerializer
from .models import Responses

class ResponsesList(generics.ListCreateAPIView):
    '''
    This class defines creation property of the api.
    '''
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializer

class ResponsesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializer

class UserStoriesView(generics.RetrieveAPIView):
    serializer_class = UserStoriesSerializer
    lookup_field = 'fb_id'
    queryset = Responses.objects.all()