# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status

from models import Responses

class ModelTestCase(TestCase):
    '''Defines the test suit for Responses model'''

    def setUp(self):
        '''Defines test client and test variable'''
        self.responses = Responses(title="Story Title", why="Story Cause", when="2017-9-16", where="Location",
                            who="People Involved", author="Author Name", author_id="Facebook ID",
                            media="Image")
    def test_respones_can_create_stories(self):
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
        assert "Location" in self.responses.where

    def test_model_resposes_who(self):
        assert "People Involved" in self.responses.who

    def test_model_resposes_author(self):
        assert "Author Name" in self.responses.author

    def test_model_resposes_author_id(self):
        assert "Facebook ID" in self.responses.author_id

    def test_model_resposes_media(self):
        assert "Image" in self.responses.media

class ViewTestCase(TestCase):
    '''Defines test suite for the api views.'''

    def setUp(self):
        '''Defines test client and test variables'''
        self.client = APIClient()
        self.story_data = {
            "title": "Story Title",
            "why": "Story Cause",
            "when": "2017-9-16",
            "where": "Location",
            "who": "People Involved",
            "author": "Author Name",
            "author_id": "Facebook ID",
            "media": "Image"
        }
        self.response = self.client.post(
            reverse('create'),
            self.story_data,
            format="json")