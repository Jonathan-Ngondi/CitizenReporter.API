# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from user_auth.models import ReporterProfile

# Create your tests here.


class BaseTestClass(TestCase):
    def setUp(self):
        self.profile = ReporterProfile.objects.create(
            name="Phillip Ahereza",
            fb_id="221DSDSD2343422342",
            fcm_token="23e24332sdksjdnfjafewrwrerwr22",
            profile_pic="https://fsdfs.com/hdjffdfd.jpg"
        )


class TestModel(BaseTestClass):
    def test_profile_created(self):
        profiles = len(ReporterProfile.objects.all())
        self.assertGreater(profiles, 0)

    def test_profile_created_with_right_info(self):
        profile = ReporterProfile.objects.latest('id')
        self.assertEqual(profile.name, "Phillip Ahereza")
        self.assertEqual(profile.fb_id, "221DSDSD2343422342")
        self.assertEqual(profile.fcm_token, "23e24332sdksjdnfjafewrwrerwr22")
        self.assertEqual(profile.profile_pic, "https://fsdfs.com/hdjffdfd.jpg")

