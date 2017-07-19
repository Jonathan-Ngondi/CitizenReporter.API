from __future__ import unicode_literals
from django.db import models

class Responses(models.Model):
    '''Creates a model containing information about the story/stories submitted by users.'''
    MEDIA_CHOICES = (('Image','image'),('Audio','audio'),('Video','video'))

    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(null=False, max_length=250)
    why = models.TextField()
    when = models.DateTimeField(auto_now_add=False)
    where = models.CharField(max_length=500)
    who = models.TextField()
    author = models.CharField(max_length=250)
    author_id = models.CharField(max_length=250)
    media = models.CharField(choices=MEDIA_CHOICES, default=None, max_length=50)

    class Meta:
        ordering = ('created',)
