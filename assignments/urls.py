from django.conf.urls import url

from assignments import views

# URLs for getting all assignments and getting assignments by id
urlpatterns = [
    url(r'^assignments$', views.AssignmentList.as_view(), name='list'),
    url(r'^assignments/(?P<pk>[0-9]+)$',
        views.AssignmentDetail.as_view(), name='detail')

]
