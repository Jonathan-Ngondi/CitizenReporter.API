# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
        print url
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


