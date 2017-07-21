# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status

from .models import Responses
from .views import ResponsesList, ResponsesDetail

class ModelTestCase(TestCase):
    '''Defines the test suit for Responses model'''

    def setUp(self):
        '''Defines test client and test variable'''
        self.responses = Responses(title="Story Title", why="Story Cause", when="2017-9-16", where="23.4",
                            who="People Involved", author="Author Name", author_id="Facebook ID", media="Image")

    def test_model_create_stories(self):
        old_count = Responses.objects.count()
        self.responses.save()
        new_count = Responses.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_resposes_title(self):
        assert "Story Title" in self.responses.title

    def test_model_resposes_why(self):
        assert "Story Cause" in self.responses.why

    def test_model_resposes_when(self):
        assert "2017-9-16" in self.responses.when

    def test_model_resposes_where(self):
        assert "23.4" in self.responses.where

    def test_model_resposes_who(self):
        assert "People Involved" in self.responses.who

    def test_model_resposes_author(self):
        assert "Author Name" in self.responses.author

    def test_model_resposes_author_id(self):
        assert "Facebook ID" in self.responses.author_id

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
            "media": None
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
        story = Responses.objects.get()
        response = self.client.get(
            '/stories/', format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, story)

    def test_update_story(self):
        '''Test api can update story.'''
        story = Responses.objects.get()
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
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_story(self):
        '''Test api can delete story.'''
        story = Responses.objects.get()
        response = self.client.delete(
            reverse('details', args=(1,)),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)