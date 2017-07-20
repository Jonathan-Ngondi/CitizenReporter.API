from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from stories import views

urlpatterns = [
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^stories/$', views.ResponsesList.as_view(), name="create"),
    url(r'^stories/user/$', views.UserList.as_view(), name="user-list"),
    url(r'^stories/(?P<pk>[0-9]+)/$', views.ResponsesDetail.as_view(), name="details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)