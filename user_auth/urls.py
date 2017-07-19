from django.conf.urls import url

from user_auth.views import RegisterProfileView, UpdateFCMView

urlpatterns = [
    url(r'^register/', RegisterProfileView.as_view(), name="register-profile"),
    url(r'^update-fcm/(?P<fb_id>\w+)/$', UpdateFCMView.as_view(),
        name="update-fcm")
]
