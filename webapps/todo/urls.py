from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^add-todo-item$', views.add_todo_item, name='add_todo_item'),
    url(r'^delete-todo-item/(?P<item_id>\d+)$', views.delete_todo_item, name='delete_todo_item'),
    # Route for built-in authentication with our own custom login page
    url(r'^login$', auth_views.login, {'template_name':'login.html'}, name='login'),
    # Route to logout a user and send them back to the login page
    url(r'^logout$', auth_views.logout_then_login, name='logout'),
    url(r'^register$', views.register, name='register'),
]
