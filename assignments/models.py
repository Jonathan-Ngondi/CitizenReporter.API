from django.db import models

class Assignment(models.Model):
    """This class creates a model for Citizen Reporter's reporting assignments."""
    # Create the list of acceptable media types for the required_media variable
    MEDIA_CHOICES = (('Image','image'),('Audio','audio'),('Video','video'))
    
    # Required Assignment class attributes 
    created = models.DateTimeField(auto_now_add=True)
    id = models.IntegerField(primary_key=True, blank=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    required_media = models.CharField(max_length=5, choices=MEDIA_CHOICES, default="Image")
    number_of_responses = models.IntegerField(blank=True)
    deadline = models.DateField()
    author = models.CharField(max_length=100, default="Anonymous")
    assignment_location= models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ('created',)
