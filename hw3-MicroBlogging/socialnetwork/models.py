from django.db import models

# User class for built-in authentication module
from django.contrib.auth.models import User

class PostItem(models.Model):
    text = models.CharField(max_length=160)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.text
    def __str__(self):
        return self.__unicode__()

