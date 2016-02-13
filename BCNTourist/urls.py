from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'BCNTourist.views.home', name='home'),

    url(r'^', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
]
