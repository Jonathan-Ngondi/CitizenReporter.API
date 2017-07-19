# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ReporterProfile(models.Model):
    name = models.CharField(max_length=200, blank=True)
    profile_pic = models.CharField(max_length=200, blank=True)
    fb_id = models.CharField(max_length=100, blank=True, unique=True)
    fcm_token = models.CharField(max_length=100, blank=True, unique=True)
