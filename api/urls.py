"""CitizenReporter_API URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

import authentication.urls as user_urls
from django.conf import settings

urlpatterns = [
    url(r'^$', include('rest_framework_docs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'api/users/', include(user_urls, namespace="user")),
    url(r'^api/assignments/',
        include('assignments.urls', namespace='assignments')),
    url(r'^api/stories/', include('stories.urls', namespace='stories')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)