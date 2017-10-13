# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authentication.models import ReporterProfile

# Create your tests here.


class TestModel(APITestCase):
    def setUp(self):
        self.profile = ReporterProfile.objects.create(
            name="Phillip Ahereza",
            uid="221DSDSD2343422342",
            fcm_token="23e24332sdksjdnfjafewrwrerwr22",
            profile_pic="https://fsdfs.com/hdjffdfd.jpg"
        )

    def test_profile_created(self):
        profiles = len(ReporterProfile.objects.all())
        self.assertGreater(profiles, 0)

    def test_profile_created_with_right_info(self):
        profile = ReporterProfile.objects.latest('id')
        self.assertEqual(profile.name, "Phillip Ahereza")
        self.assertEqual(profile.uid, "221DSDSD2343422342")
        self.assertEqual(profile.fcm_token, "23e24332sdksjdnfjafewrwrerwr22")
        self.assertEqual(profile.profile_pic, "https://fsdfs.com/hdjffdfd.jpg")


class TestRegisterProfile(APITestCase):
    """
    After facebook public profile after user authentication on API
    consuming clients
    """

    def setUp(self):
        self.url = reverse('user:register-profile')
        self.data = {
            "name": "Phillip Ahereza",
            "uid": "221DSDSD2343422342",
            "profile_pic": "https://fsdfs.com/hdjffdfd.jpg",
        }

    def test_register_profile(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        profile = ReporterProfile.objects.latest('id')
        self.assertEqual(profile.name, "Phillip Ahereza")
        self.assertEqual(profile.uid, "221DSDSD2343422342")
        self.assertEqual(profile.profile_pic, "https://fsdfs.com/hdjffdfd.jpg")

    def test_register_preexisting_profile(self):
        # register profile
        self.client.post(self.url, self.data)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_add_another_user(self):
        self.client.post(self.url, {
            "name": "Phillip Ahereza",
            "uid": "221DSDSD234",
            "profile_pic": "https://fsdfs.com/hdjffdfd.jpg",
        })
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ReporterProfile.objects.count(), 2)


class TestUpdateFCM(APITestCase):
    def setUp(self):
        self.profile = ReporterProfile.objects.create(
            name="Phillip Ahereza",
            uid="221DSDSD2343422342",
            fcm_token="23e24332sdksjdnfjafewrwrerwr22",
            profile_pic="https://fsdfs.com/hdjffdfd.jpg"
        )

    def test_update_fcm_id(self):
        profile = ReporterProfile.objects.latest('id')
        url = reverse('user:update', kwargs={'uid': profile.uid})
        data = {
            'fcm_token': '1234567890'
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_profile = ReporterProfile.objects.latest('id')
        self.assertEqual(updated_profile.name, "Phillip Ahereza")
        self.assertEqual(updated_profile.uid, "221DSDSD2343422342")
        self.assertEqual(updated_profile.profile_pic,
                         "https://fsdfs.com/hdjffdfd.jpg")
        self.assertEqual(updated_profile.fcm_token, '1234567890')


class TestUpdateLocation(APITestCase):
    def setUp(self):
        self.profile = ReporterProfile.objects.create(
            name="Phillip Ahereza",
            uid="221DSDSD2343422342",
            fcm_token="23e24332sdksjdnfjafewrwrerwr22",
            profile_pic="https://fsdfs.com/hdjffdfd.jpg",
            location=""
        )

    def test_update_location(self):
        profile = ReporterProfile.objects.latest('id')
        url = reverse('user:update', kwargs={'uid': profile.uid})
        print(url)
        data = {
            'location': '32, 23'
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_profile = ReporterProfile.objects.latest('id')
        self.assertEqual(updated_profile.name, "Phillip Ahereza")
        self.assertEqual(updated_profile.uid, "221DSDSD2343422342")
        self.assertEqual(updated_profile.profile_pic,
                         "https://fsdfs.com/hdjffdfd.jpg")
        self.assertEqual(updated_profile.location, '32, 23')