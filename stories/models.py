from __future__ import unicode_literals
from django.db import models

from api.settings import MEDIA_URL
from utils import scramble_uploaded_filename


class Story(models.Model):
    """
    Creates a model containing information about the story/stories submitted
    by users.
    """

    id = models.IntegerField(primary_key=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    local_id = models.IntegerField(default=0)
    assignmentId = models.IntegerField(default=0)
    title = models.CharField(null=False, max_length=250)
    summary = models.TextField()
    when = models.CharField(max_length=20, default="")
    where = models.CharField(max_length=200, default='Unkown')
    who = models.TextField()
    author = models.CharField(max_length=250, default="Anonymous")
    fb_id = models.CharField(max_length=250, default="unknown")
    uploaded = models.BooleanField(default=True)
    updated = models.CharField(max_length=30, default="unknown")
    local_media_paths = models.TextField(max_length=5000, default="")



    class Meta:
        ordering = ('created',)

class Media(models.Model):
    '''Creates model for media uploads'''

    response = models.ForeignKey(Response, related_name='media_uploads')
    media_upload = models.FileField(upload_to='uploads/', null=True, blank=True)

    story = models.ForeignKey(Story, related_name='media')
    file = models.FileField(upload_to=scramble_uploaded_filename, null=True,
                            blank=True)

    def __unicode__(self):
        return "{0}{1}".format(MEDIA_URL, self.file.url)

