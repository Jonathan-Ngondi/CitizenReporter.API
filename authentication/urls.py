from django.conf.urls import url

from authentication.views import RegisterProfileView, UpdateFCMView, ListUsers

urlpatterns = [
    url(r'^register$', RegisterProfileView.as_view(), name="register-profile"),
    url(r'^$', ListUsers.as_view(), name="list"),
    url(r'^update/(?P<uid>\w+)/$', UpdateFCMView.as_view(),
        name="update")
]
