from __future__ import unicode_literals
from django.db import models

class Response(models.Model):
    '''Creates a model containing information about the story/stories submitted by users.'''

    id = models.IntegerField(primary_key=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(null=False, max_length=250)
    why = models.TextField()
    when = models.DateTimeField(auto_now_add=False)
    where = models.DecimalField(max_digits=9, decimal_places=6)
    who = models.TextField()
    author = models.CharField(max_length=250, default="Anonymous")
    author_id = models.CharField(max_length=250)
    media = models.FileField(upload_to='uploads/', null=True, blank=True)

    def get_media(self):
        '''Returns all the media uploads.'''
        return self.media

    class Meta:
        ordering = ('created',)

class Media(models.Model):
    '''Creates model for media uploads'''
    response = models.ForeignKey(Response, related_name='media_uploads')
    media_upload = models.FileField(upload_to='uploads/', null=True, blank=True)


