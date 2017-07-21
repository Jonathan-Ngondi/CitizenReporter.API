from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from stories import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^stories/$', views.ResponsesList.as_view(), name="create"),
    url(r'^stories/user/(?P<fb_id>[0-9]+)/$', views.UserStoriesView.as_view(), name="details"),
    url(r'^stories/(?P<pk>[0-9]+)/$', views.ResponsesDetail.as_view(), name="details"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)