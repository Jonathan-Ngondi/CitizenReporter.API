# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, \
    ListAPIView
from rest_framework.response import Response

from authentication.models import ReporterProfile
from authentication.serializers import UpdateSerializer, \
    ProfileCreateSerializer, ProfileListSerializer


# Create your views here.


class RegisterProfileView(CreateAPIView):
    serializer_class = ProfileCreateSerializer

    def post(self, request, *args, **kwargs):
        """
        save the profile only and only if the uid is unique
        """
        uid = request.data['uid']
        num_results = ReporterProfile.objects.filter(
            uid=uid).count()

        if num_results == 0:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED, headers=headers)

        else:
            return Response(status=status.HTTP_202_ACCEPTED)


class UpdateFCMView(RetrieveUpdateAPIView):
    serializer_class = UpdateSerializer
    lookup_field = 'uid'
    queryset = ReporterProfile.objects.all()


class ListUsers(ListAPIView):
    serializer_class = ProfileListSerializer
    queryset = ReporterProfile.objects.all()