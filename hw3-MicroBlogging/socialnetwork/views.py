from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from socialnetwork.models import *
from socialnetwork.forms import *


@login_required
def global_home(request):
    # Get all posts of users in system sorted in descending order
    items = PostItem.objects.all().order_by('-date') 
    #Sort by date in chronological order
    return render(request, 'index.html', {'items' : items})


@login_required
def user_home(request):
    # Get all posts of the logged in user sorted in descending order
    items = PostItem.objects.filter(user=request.user).order_by('-date')
    return render(request, 'profile-page.html', {'items' : items, 'user': request.user, 'read_only':False })

@login_required
def user_profile(request,user_id):
    # get user profile
    user = User.objects.get(id=user_id)
    # redirect user to own page
    if(user == request.user):
        return redirect('home')
    #get other user's post
    items = PostItem.objects.filter(user=user).order_by('-date')
    #Set is_owner to false and disable posting
    context = {'items' : items, 'user': user, 'read_only':True }
    return render(request, 'profile-page.html', context)

@login_required
@transaction.atomic
def post_item(request):
    error = ''
    # Creates a new item if a post is present as a parameter in the request
    if not 'item' in request.POST or not request.POST['item']:
        error ='You must enter an item to add.'
    # Check if length is greater than 160    
    elif 'item' in request.POST and len(request.POST['item']) > 160:
        error = 'Text is too long. Must not be greater than 160'
    else:
        new_item = PostItem(text=request.POST['item'], user=request.user)
        new_item.save()

     # redirect user to own page
    if(len(error) == ''):
        return redirect('home')

    items = PostItem.objects.filter(user=request.user)
    context = {'items' : items, 'post_error' : error, 'user': request.user}
    return render(request, 'profile-page.html', context)


@transaction.atomic
def register(request):
    context = {}

    # Display the registration form if it is a GET request.
    if request.method == 'GET':
        context['form'] = RegistrationForm()
        return render(request, 'register.html', context)

    # Creates form from the request POST parameters and makes the 
    # form available in the request context dictionary.
    form = RegistrationForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'register.html', context)

    # If form data is valid. Register and login the user.
    new_user = User.objects.create_user(username=form.cleaned_data['username'], \
                                        password=form.cleaned_data['password1'],\
                                        first_name = form.cleaned_data['first_name'],\
                                        last_name = form.cleaned_data['last_name'] )
    new_user.save()

    # Logs in the new user and redirects to his/her todo list
    new_user = authenticate(username=form.cleaned_data['username'], \
                            password=form.cleaned_data['password1'], \
                            first_name = form.cleaned_data['first_name'],\
                            last_name = form.cleaned_data['last_name'] )
    login(request, new_user)
    return redirect('home')
    
