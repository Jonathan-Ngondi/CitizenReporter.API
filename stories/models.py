from __future__ import unicode_literals
from django.db import models

class Responses(models.Model):
    '''Creates a model containing information about the story/stories submitted by users.'''

    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(null=False, max_length=250)
    why = models.TextField()
    when = models.DateTimeField(auto_now_add=False)
    # where = 
    who = models.TextField()
    author = models.CharField(null=False, max_length=250)
    #author_id = models.IntegerField(primary_key=True)
    #media = 

    class Meta:
        ordering = ('created',)
