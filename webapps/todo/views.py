from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
#import the model
from todo.models import *

def home(request):
	#get all items
	all_items = TodoItem.objects.all()

	return render(request, 'index.html',{'items':all_items})

def add_todo_item(request):

	return render(request, 'index.html',{})

def delete_todo_item(request,item_id):
	return render(request, 'index.html',{})
