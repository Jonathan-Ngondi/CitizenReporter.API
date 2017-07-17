from django.db import models

class Assignments(models.Model):
    """This class creates a model for Citizen Reporter's reporting assignments."""
    media_types = ['image','audio','video']

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    required_media = models.CharField(max_length=5, choices=media_types, default=None)
    number_of_responset = models.IntegerField()
    deadline = models.DateField()

