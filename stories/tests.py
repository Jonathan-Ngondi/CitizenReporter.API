# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

import shutil

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from stories.models import Media, Story
from utils import generate_photo_file


class StoryModelTestCase(TestCase):
    """Defines the test suit for Responses model"""

    def setUp(self):
        """Defines test client and test variable"""
        self.item = Story.objects.create(title="Story Title",
                                         summary="Story Cause",
                                         when="2017-9-16",
                                         where="23.4",
                                         who="People Involved",
                                         author="Author Name",
                                         fb_id="fb_id",
                                         local_media_paths="Image"
                                         )

    def test_model_create_stories(self):
        self.assertEqual(1, Story.objects.count())

    def test_model_responses_title(self):
        assert "Story Title" in self.item.title

    def test_model_responses_why(self):
        assert "Story Cause" in self.item.summary

    def test_model_responses_when(self):
        assert "2017-9-16" in self.item.when

    def test_model_resposes_where(self):
        assert "23.4" in self.item.where

    def test_model_responses_who(self):
        assert "People Involved" in self.item.who

    def test_model_responses_author(self):
        assert "Author Name" in self.item.author

    def test_model_responses_fb_id(self):
        assert "fb_id" in self.item.fb_id


class StoryTestAPI(APITestCase):
    def setUp(self):
        self.story_data = {
            "title": "Story Title",
            "summary": "Story Cause",
            "when": "2017-9-16 00:30",
            "where": "23.33",
            "who": "People Involved",
            "author": "Author Name",
            "fb_id": "123456789",
            "updated": "12 August 2017",
            "local_media_paths": "Image"
        }

    def tearDown(self):
        try:
            shutil.rmtree('MediaUploads')
        except OSError:
            pass

    def test_create_story(self):
        url = reverse('stories:create')
        print(url)
        response = self.client.post(url, self.story_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_media_upload(self):
        url = reverse('stories:create')
        response = self.client.post(url, self.story_data)
        if response.status_code == status.HTTP_201_CREATED:
            story_id = response.data[u'id']
            media_url = reverse('stories:media')
            media_response = self.client.post(media_url, {
                "story": story_id,
                "file": generate_photo_file()
            })
            self.assertEqual(media_response.status_code,
                             status.HTTP_201_CREATED)
            self.assertEqual(Media.objects.count(), 1)

    def test_retrieve_stories(self):
        url = reverse('stories:create')
        response = self.client.post(url, self.story_data)
        story_id = response.data['id']
        media_url = reverse('stories:media')
        for i in range(0, 3):
            self.client.post(media_url, {
                "story": story_id,
                "file": generate_photo_file()
            })

        retrieve_url = reverse('stories:create')
        response = self.client.get(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Media.objects.count(), 3)


class UserStoriesTest(APITestCase):
    def setUp(self):
        story1 = Story.objects.create(title="Story Title",
                                      summary="Story Cause",
                                      when="2017-9-16",
                                      where="23.4",
                                      who="People Involved",
                                      local_media_paths="Image",
                                      author="Author Name",
                                      local_id="23",
                                      fb_id="123456789",
                                      uploaded=True,
                                      updated="12 August 2017"
                                      )

        story2 = Story.objects.create(title="Story Title 2",
                                      summary="Story Cause 2",
                                      when="2017-9-16", where="23.4",
                                      who="People Involved",
                                      author="Author Name",
                                      local_id="23",
                                      fb_id="123456789",
                                      uploaded=True,
                                      updated="12 August 2017",
                                      local_media_paths="Image")
        media_url = reverse('stories:media')
        for i in range(0, 3):
            self.client.post(media_url, {
                "story": story1.id,
                "file": generate_photo_file()
            })

        for i in range(0, 3):
            self.client.post(media_url, {
                "story": story2.id,
                "file": generate_photo_file()
            })

    def test_get_user_stories(self):
        url = reverse('stories:user-stories', kwargs={'fb_id': '123456789'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_user_no_stories(self):
        url = reverse('stories:user-stories', kwargs={'fb_id': '12567890'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


class ParseStoryTest(APITestCase):
    """This tests tests that the Parse Webhook uploads a story to
    the API after saving the Story in Parse.
    """

    def setUp(self):
        self.parse_story = {
    "triggerName": "afterSave",
    "object": {
        "when": {
            "__type": "Date",
            "iso": "2017-10-03T12:14:52.593Z"
        },
        "title": "Baga",
        "who": "Me",
        "location": "Andela Kenya",
        "assignment": "5dOOMjWo2u",
        "uploaded": "true",
        "localID": "d31e17fd-a70b-4083-b04d-4c05cab266fa",
        "summary": "Yup",
        "media": [
            {
                "__type": "File",
                "name": "f54d6bee2fffddd5a1df2c26a8c5586a_IMG-20171003-WA0019.jpg",
                "url": "http://creporter-server.herokuapp.com/parse/files/11235813/f54d\
                6bee2fffddd5a1df2c26a8c5586a_IMG-20171003-WA0019.jpg"
            },
            {
                "__type": "File",
                "name": "66cb1dee3df2d7d3aff2a5cffd05f103_IMG-20171003-WA0018.jpg",
                "url": "http://creporter-server.herokuapp.com/parse/files/11235813/66cb\
                1dee3df2d7d3aff2a5cffd05f103_IMG-20171003-WA0018.jpg"
            },
            {
                "__type": "File",
                "name": "f8df0f1ff10c6d9c16e51ac8ac8966c6_IMG-20171003-WA0020.jpg",
                "url": "http://creporter-server.herokuapp.com/parse/files/11235813/f8df\
                0f1ff10c6d9c16e51ac8ac8966c6_IMG-20171003-WA0020.jpg"
            }
        ],
        "author": "QiR90vrhcR",
        "createdAt": "2017-10-03T12:14:57.511Z",
        "updatedAt": "2017-10-03T12:14:57.511Z",
        "objectId": "EDiV5IwzMc",
        "className": "Story"
    },
    "master": "false",
    "log": {
        "appId": "11235813"
    },
    "headers": {
        "host": "creporter-server.herokuapp.com",
        "connection": "close",
        "x-parse-session-token": "r:bc62398c1da0ad288f55b025c51e5aeb",
        "x-parse-application-id": "11235813",
        "x-parse-client-version": "a1.15.7",
        "x-parse-app-build-version": "1",
        "x-parse-app-display-version": "1.3-beta",
        "x-parse-os-version": "6.0",
        "user-agent": "Parse Android SDK 1.15.7 (org.codeforafrica.citizenreporterandroid/1) API Level 23",
        "x-parse-installation-id": "7b96b0e1-fa59-4899-a942-825a69fbea28",
        "content-type": "application/json",
        "accept-encoding": "gzip",
        "x-request-id": "0ed31771-b0d2-4f56-b2cf-f692b105474a",
        "x-forwarded-for": "154.123.178.211",
        "x-forwarded-proto": "http",
        "x-forwarded-port": "80",
        "via": "1.1 vegur",
        "connect-time": "0",
        "x-request-start": "1507032897482",
        "total-route-time": "0",
        "content-length": "377"
    },
    "user": {
        "name": "Jim",
        "username": "jim@email.com",
        "email": "jim@email.com",
        "createdAt": "2017-09-21T08:21:28.007Z",
        "updatedAt": "2017-10-03T12:09:01.551Z",
        "fcm_token": "d84vsHomaz4:APA91bGc_CJnUItY8mDARvF2CLjn7FOxPU16bB0uZr7DLoZ1pgw3T8NVC3b7dDI945lrZ2OgoLs6_cwUDfCWV1lgILFKchPhggn6dEV89z67c5-Qicn3Nx7Xcb95wdqKJ4X3t8wLdkoi",
        "ACL": {
            "*": {
                "read": "true"
            },
            "QiR90vrhcR": {
                "read": "true",
                "write": "true"
            }
        },
        "sessionToken": "r:bc62398c1da0ad288f55b025c51e5aeb",
        "objectId": "QiR90vrhcR"
    },
            "installationId": "7b96b0e1-fa59-4899-a942-825a69fbea28"
    }

    def test_post_webhook_parse(self):
        """Tests whether the app will post parse story objects to our Django endpoint."""
        url = reverse('stories:parse')
        response = self.client.post(url, data=self.parse_story, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
   
    def test_post_webhook_media(self):
        """Test whether multiple media urls will get posted to the endpoint."""
        url = reverse('stories:parse')
        response = self.client.post(url, data=self.parse_story, format='json')
        self.assertIn("http://creporter-server.herokuapp.com/parse/files/11235813/66cb1dee3df2d7d3\
        aff2a5cffd05f103_IMG-20171003-WA0018.jpg",
                      response.data["local_media_paths"])
        self.assertIn("http://creporter-server.herokuapp.com/parse/files/11235813/f8df0f1ff10c6d9c\
        16e51ac8ac8966c6_IMG-20171003-WA0020.jpg",
                      response.data["local_media_paths"])
        self.assertIn("http://creporter-server.herokuapp.com/parse/files/11235813/f8df0f1ff10c6d9c1\
        6e51ac8ac8966c6_IMG-20171003-WA0020.jpg",
                      response.data["local_media_paths"])
        