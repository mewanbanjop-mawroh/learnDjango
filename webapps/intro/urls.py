from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^hello-world$', 'intro.views.hello_world'),
    url(r'^hello.html$', 'intro.views.hello'),
]
