from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from feeds import LatestEntryFeed

from stories import views

urlpatterns = [
    url(r'^$', views.StoryCreateView.as_view(),
        name="create"),
    url(r'^media/$', views.MediaUploadView.as_view(),
        name="media"),
    url(r'^user/(?P<fb_id>[0-9]+)/$',
        views.UserStoriesView.as_view(), name="user-stories"),
    url(r'^(?P<pk>[0-9]+)/$',
        views.StoriesDetailView.as_view(), name="details"),
    url(r'^feeds/', LatestEntryFeed()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
