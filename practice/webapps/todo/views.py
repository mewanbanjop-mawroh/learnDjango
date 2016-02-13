from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
#import the model
from todo.models import *
# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required
# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate



def home(request):
    # Sets up list of just the logged-in user's (request.user's) items
    items = Item.objects.filter(user=request.user) 
    return render(request, 'index.html', {'items' : items})

@login_required
def index(request):
	# get all itemsSets of the logged-in user's (request.user's) items
    all_items = TodoItem.objects.filter(user=request.user)
	return render(request, 'index.html',{'items':all_items})

@login_required
def add_todo_item(request):
	errors = [] #list to record errors
	if not 'item' in request.POST or not request.POST['item']:
		errors.append('You should add an item')
	else:
		new_item = TodoItem(text=request.POST['item'], user=request.user)
		new_item.save()

	return render(request, 'index.html',{'items':TodoItem.objects.filter(user=request.user), 'errors': errors})

@login_required
def delete_todo_item(request,item_id):
	errors = []
	try:
		item_to_delete = TodoItem.objects.get(id = item_id, user=request.user)
		item_to_delete.delete()
	except ObjectDoesNotExist:
		errors.append('The item did not exist in the todo list.')

    	items = TodoItem.objects.filter(user=request.user)
    	context = {'items':items, 'errors':errors}
	return render(request, 'index.html',context)


def register(request):
    context = {}

    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = RegistrationForm()
        return render(request, 'register.html', context)

    # Creates a bound form from the request POST parameters and makes the 
    # form available in the request context dictionary.
    form = RegistrationForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'register.html', context)

    # If we get here the form data was valid.  Register and login the user.
    new_user = User.objects.create_user(username=form.cleaned_data['username'], \
                                        password=form.cleaned_data['password1'])
    new_user.save()

    # Logs in the new user and redirects to his/her todo list
    new_user = authenticate(username=form.cleaned_data['username'], \
                            password=form.cleaned_data['password1'])
    login(request, new_user)
    return redirect('/todo/')
