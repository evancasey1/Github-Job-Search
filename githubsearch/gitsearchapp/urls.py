# app/urls.py

from django.conf.urls import url
from gitsearchapp import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^profile/$', views.profile, name='profile'),
]

