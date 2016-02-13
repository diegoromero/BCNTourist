from django.conf.urls import include, url
from django.contrib import admin
from api import views

urlpatterns = [
    url(r'^update/location$', views.update_location, name='update_location'),
]
