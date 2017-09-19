from django.contrib.syndication.views import Feed
from django.db import models
from django.urls import reverse

from api.urls import *
from stories.models import Story


class LatestEntryFeed(Feed):
    """
    This class creates a view for viewing an RSS Feed of the latest stories.
    """
    title = "Stories feed from Citizen Reporter"
    link = "/feeds/"
    description = "This is a feed showing all the posted stories from Citizen Reporter"

    def items(self):
        """This method returns the 5 most recent stories."""
        return Story.objects.order_by('-created')[:5]

    # The following 2 methods determine the way the Feed items appear
    def item_title(self, item):
        """This returns the title for every item in the RSS feed."""
        return item.title

    def item_description(self, item):
        """This returns the summary for every item in the RSS feed."""
        return item.summary

    def item_link(self, item):
        """This returns the url for every item in the RSS feed."""
        return item.get_absolute_url()
