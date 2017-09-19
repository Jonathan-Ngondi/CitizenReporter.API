from django.conf.urls import url

from authentication.views import ListUsers, RegisterProfileView, UpdateFCMView

# Urls allowing the user to register, list and update profiles to the api
urlpatterns = [
    url(r'^register$', RegisterProfileView.as_view(), name="register-profile"),
    url(r'^$', ListUsers.as_view(), name="list"),
    url(r'^update/(?P<fb_id>\w+)/$', UpdateFCMView.as_view(),
        name="update")
]
