# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ReporterProfile(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    profile_pic = models.CharField(max_length=200, blank=False, null=False)
    uid = models.CharField(max_length=100,
                             unique=True, blank=False, null=False)
    fcm_token = models.CharField(
        max_length=100, default=" ", null=True, blank=True)

    location = models.CharField(
        max_length=100, default=" ", null=True, blank=True)
