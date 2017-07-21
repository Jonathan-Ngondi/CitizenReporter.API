# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics

from .serializers import ResponseSerializer, UserStoriesSerializer
from .models import Response

class ResponsesList(generics.ListCreateAPIView):
    '''
    This class defines creation property of the api.
    '''
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

class ResponsesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

class UserStoriesView(generics.RetrieveAPIView):
    serializer_class = UserStoriesSerializer
    lookup_field = 'fb_id'
    queryset = Response.objects.all()