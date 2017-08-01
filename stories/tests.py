# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import  APIClient
from rest_framework import status

import shutil

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from stories.models import Media, Story
from utils import generate_photo_file



from .models import Response
from .views import ResponsesList, ResponsesDetail, UserStoriesView

class StoryModelTestCase(TestCase):
    """Defines the test suit for Responses model"""

    def setUp(self):
        """Defines test client and test variable"""

        self.item = Story.objects.create(title="Story Title",
                                         why="Story Cause",
                                         when="2017-9-16", where="23.4",
                                         who="People Involved",
                                         author="Author Name",
                                         fb_id="fb_id",
                                         local_media_paths="Image")


    def test_model_create_stories(self):
        old_count = Response.objects.count()
        self.response.save()
        new_count = Response.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_resposes_title(self):
        assert "Story Title" in self.response.title

    def test_model_resposes_why(self):
        assert "Story Cause" in self.response.why

    def test_model_resposes_when(self):
        assert "2017-9-16" in self.response.when

    def test_model_resposes_where(self):
        assert "23.4" in self.response.where

    def test_model_resposes_who(self):
        assert "People Involved" in self.response.who

    def test_model_resposes_author(self):
        assert "Author Name" in self.response.author

    def test_model_responses_fb_id(self):
        assert "fb_id" in self.item.fb_id


class ViewTestCase(TestCase):
    '''Defines test suite for the api views.'''

    def setUp(self):
        '''Defines test client and test variables'''
        self.client = APIClient()
        self.story_data = {
            "title": "Story Title",
            "why": "Story Cause",
            "when": "2017-9-16 00:30",
            "where": "23.33",
            "who": "People Involved",
            "author": "Author Name",
            "author_id": "Facebook ID",
            "media": None,

            "fb_id": "123456789",
            "local_media_paths": ""

        }
        self.response = self.client.post(
            reverse('create'),
            self.story_data,
            format="json")

    def test_create_story(self):
        '''Test api can create story'''
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_get_stories(self):
        '''Test if api can get list of stories.'''
        story = Response.objects.get()
        response = self.client.get(self.story_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, story)


    def test_update_story(self):
        '''Test api can update story.'''
        story = Response.objects.get()
        new_story = {
            "title": "New Title",
            "why": "Story Cause",
            "when": "2017-9-16 00:30",
            "where": "23.33",
            "who": "People Involved",
            "author": "Author Name",
            "author_id": "Facebook ID",
            "media": None
        }
        response = self.client.put(
            reverse('details', args=(1,)),
            new_story, format='json'
        )


    def test_create_story(self):
        url = reverse('stories:create')
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


    def test_delete_story(self):
        '''Test api can delete story.'''
        story = Response.objects.get()
        response = self.client.delete(
            reverse('details', args=(1,)),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Media.objects.count(), 3)


class UserStoriesTest(APITestCase):
    def setUp(self):
        story1 = Story.objects.create(title="Story Title",
                                      why="Story Cause",
                                      when="2017-9-16", where="23.4",
                                      who="People Involved",
                                      author="Author Name",
                                      fb_id="123456789",
                                      local_media_paths="Image")

        story2 = Story.objects.create(title="Story Title 2",
                                      why="Story Cause 2",
                                      when="2017-9-16", where="23.4",
                                      who="People Involved",
                                      author="Author Name",
                                      fb_id="123456789",
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


