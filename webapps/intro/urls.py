from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello-world$', views.hello_world, name='hello_world'),
]

# --Deprecated-- 
#from django.conf.urls import url
# urlpatterns = [
# url(r'^hello-world$', 'intro.views.hello_world'),
# ]