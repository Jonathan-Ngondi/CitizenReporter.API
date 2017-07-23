from __future__ import unicode_literals

from django.db import models

from CitizenReporter_API.settings import MEDIA_URL


class Story(models.Model):
    """
    Creates a model containing information about the story/stories submitted
    by users.
    """

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(null=False, max_length=250)
    why = models.TextField()
    when = models.CharField(max_length=20, default="")
    where = models.CharField(max_length=200, default='Unkown')
    who = models.TextField()
    author = models.CharField(max_length=250, default="Anonymous")
    author_id = models.CharField(max_length=250)
    local_media_paths = models.CharField(max_length=5000, default="")

    class Meta:
        ordering = ('created',)


class Media(models.Model):
    '''Creates model for media uploads'''
    story = models.ForeignKey(Story, related_name='media')
    file = models.FileField(upload_to='uploads/', null=True, blank=True)

    def __unicode__(self):
        return "{0}{1}".format(MEDIA_URL, self.file.url)
