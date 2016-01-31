from django.db import models
#Data model for todo item
class TodoItem(models.Model): #inherit from models django orm
	text = models.CharField(max_length=200)
	# function to generate unicode string
	def __unicode__(self):
		return self.text
		
