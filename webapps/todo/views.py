from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html',{})

def add_todo_item(request):
	return render(request, 'index.html',{})

def delete_todo_item(request,item_id):
	return render(request, 'index.html',{})
