from django.conf.urls import include, url
from socialnetwork import views

urlpatterns = [
    url(r'', include('socialnetwork.urls')),
]
