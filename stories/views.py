# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User

from .serializers import ResponsesSerializer, UserSerializer
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

class UserList(generics.ListCreateAPIView):
    '''This class defines get methothod for a specific User'''
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return user.accounts.all()

class ResponsesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializer