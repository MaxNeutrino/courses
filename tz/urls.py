"""tz URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

from tz import views

urlpatterns = [
    url(r'^users/$', views.UserView.as_view(), name='users'),
    url(r'^courses/$', views.CourseView.as_view(), name='courses'),
    url(r'^courses/create/$', views.create_a_course, name='create_course'),
    url(r'^courses/update/(?P<course_id>[0-9]+)/$', views.update_a_course, name='update_course'),
    url(r'^courses/delete/(?P<course_id>[0-9]+)/$', views.delete_a_course, name='delete_course'),
    url(r'^users/create/$', views.create_a_user, name='create_user'),
    url(r'^users/update/(?P<user_id>[0-9]+)/$', views.update_a_user, name='update_user'),
    url(r'^users/delete/(?P<user_id>[0-9]+)/$', views.delete_a_user, name='delete_user'),
    url(r'^$', views.auth, name='auth'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^admin/', admin.site.urls),
]
