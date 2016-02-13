from django.db import models
# User class from django.contrib.auth.models for built-in authentication module
from django.contrib.auth.models import User
#Data model for todo item
class TodoItem(models.Model): #inherit from models django orm
	text = models.CharField(max_length=200)
	user = models.ForeignKey(User)
    # function to generate unicode string
    def __unicode__(self):
        return self.text
    def __str__(self):
        return self.__unicode__()
