from django.db import models

from utils import scramble_uploaded_filename


class Assignment(models.Model):
    """
    This class creates a model for Citizen Reporter's reporting assignments.
    """
    # Create the list of acceptable media types for the required_media variable
    MEDIA_CHOICES = (('Image', 'image'),
                     ('Audio', 'audio'), ('Video', 'video'),
                     ('image + video', 'image & video'),
                     ('image + audio', 'image & audio'),
                     ('audio + video', 'audio & video'),
                     ('image + audio + video', 'image & audio & video'),)

    # Required Assignment class attributes
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    required_media = models.CharField(
        max_length=5, choices=MEDIA_CHOICES, default="Image")
    featured_image = models.ImageField(
        upload_to=scramble_uploaded_filename, blank=True)
    number_of_responses = models.IntegerField(null=True, default=None)
    deadline = models.DateField()
    author = models.CharField(max_length=100, default="Anonymous")
    assignment_location = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ('created',)