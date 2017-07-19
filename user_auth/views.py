# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import IntegrityError
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response

from user_auth.models import ReporterProfile
from user_auth.serializers import FCMUpdateSerializer, ProfileCreateSerializer

# Create your views here.


class RegisterProfileView(CreateAPIView):
    serializer_class = ProfileCreateSerializer

    def post(self, request, *args, **kwargs):
        """
        save the profile only and only if the fb_id is unique
        """
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED, headers=headers)
        except IntegrityError:
            return Response(status=status.HTTP_200_OK)


class UpdateFCMView(UpdateAPIView):
    serializer_class = FCMUpdateSerializer
    lookup_field = 'fb_id'
    queryset = ReporterProfile.objects.all()
