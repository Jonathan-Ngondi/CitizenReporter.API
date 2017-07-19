from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from stories import views

urlpatterns = [
    url(r'^stories/$', views.ResponsesList.as_view(), name="Create"),
    url(r'^stories/(?P<pk>[0-9]+)/$', views.ResponsesDetail.as_view(), name="Details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)