from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from stories import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    url(r'^$', views.StoryCreateView.as_view(),
        name="create"),
    url(r'^media/$', views.MediaUploadView.as_view(),
        name="media"),
    url(r'^user/(?P<fb_id>[0-9]+)/$',
        views.UserStoriesView.as_view(), name="user-stories"),
    url(r'^(?P<pk>[0-9]+)/$',
        views.StoriesDetailView.as_view(), name="details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = format_suffix_patterns(urlpatterns)