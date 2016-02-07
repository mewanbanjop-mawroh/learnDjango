from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
#import the model
from todo.models import *

def index(request):
	#get all items
	all_items = TodoItem.objects.all()

	return render(request, 'index.html',{'items':all_items})

def add_todo_item(request):
	errors = [] #list to record errors
	if not 'item' in request.POST or not request.POST['item']:
		errors.append('You should add an item')
	else:
		new_item = TodoItem(text=request.POST['item'])
		new_item.save()

	return render(request, 'index.html',{'items':TodoItem.objects.all(), 'errors': errors})

def delete_todo_item(request,item_id):
	errors = []
	try:
		item_to_delete = TodoItem.objects.get(id = item_id)
		item_to_delete.delete()
	except ObjectDoesNotExist:
		errors.append('The item did not exist in the todo list.')

    	items = TodoItem.objects.all()
    	context = {'items':items, 'errors':errors}
	return render(request, 'index.html',context)
