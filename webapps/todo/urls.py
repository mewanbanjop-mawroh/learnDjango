from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^add-todo-item$', views.add_todo_item, name='add_todo_item'),
    url(r'^delete-todo-item/(?P<item_id>\d+)$', views.delete_todo_item, name='delete_todo_item'),
]
