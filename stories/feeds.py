from django.db import models
from django.contrib.syndication.views import Feed
from django.urls import reverse
from stories.models import Story
from api.urls import *


class LatestEntryFeed(Feed):
    """
    This class creates a view for viewing an RSS Feed of the latest stories.    
    """
    title = "Stories feed from Citizen Reporter"
    link = "/feeds/"
    description = "This is a feed showing all the posted stories from Citizen Reporter"

    def items(self):
        return Story.objects.order_by('created')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summary

    def item_link(self, item):
        return item.get_absolute_url()
