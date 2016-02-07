#Learning Python and Django
##Version
```
Python 2.7.10 
Django 1.9.1
```
## Installation and Creating new project
1. Install [python] (https://www.python.org/download/), [pip] (https://pip.pypa.io/en/stable/) and in the terminal type `pip install Django`
2. Create a new django project 
```shell
django-admin startproject project_name
```
3. Create a new web app "intro"
```shell
cd project_name/
python manage.py startapp application_name
```
## Django Project Configuration and Routing

In project_name/webapps folder there are project settings file.

1. webapps/settings.py 
	* which contain the project settings.
	* add your new application to the INSTALLED_APPS configuration
```python
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'application_name',
]
```
2. webapps/urls.py 
	* default configuration for routing Http requests.
	* add regex rule for your application route "url(r'^application_name/', application_name.urls),". The first parameter is the regex rule and the second is the location which is application_name/urls.py
```python
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^application_name/', include('application_name.urls')),
]

```

## Create your application routes 
1. Create a new file application_name/urls.py
2. add the route for your actions e.g.

```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello-world$', views.hello_world, name='hello_world'),
]
```
## Add functions in views.py to return static html file
1. Create a file hello-world.html and put it in a new folder application_name/templates
2. Add a function `hello_world` to views.py
```python
from django.shortcuts import render

#action for 'intro/hello-world' route
def hello_world(request):
	#render takes (1) the request, 
	#(2) the name of the view to generate and 
	#(3) key-value pair for template views
	return render(request,'hello-world.html',{})
```
## Run server
Type `python manage.py runserver` to start development server and enter http://127.0.0.1:8000/intro/hello-world to see if the static web page is returned

## Apply changes
After changes to python files type `python manage.py migrate` before running server. Otherwise you will get an error
```
You have unapplied migrations; your app may not work properly until they are applied. Run 'python manage.py migrate' to apply them.
```
## Creating a Todo application
1. Create the app using ```python manage.py startapp application_name```
2. Add the urls to webapps/urls.py and add to 'todo' to INSTALLED_APPS of settings.py
3. Create url.py in todo

## Data model
1. To use python ORM, define simple python classes that inherit django db models class to use the orm features of Django.
2. Define class for the data you want to store in models.py class or in separate class which you then include.
3. Django generate id and primary key automatically if we don't specify.

```python
#models.py class
from django.db import models
#Data model for todo item
class TodoItem(models.Model): #inherit from models django orm
    text = models.CharField(max_length=200)
    def __unicode__(self):
        return self.text
```       
## Create actions for todo

1. Import the model in views.py ```from todo.models import *```

2. Add index action
```python
from django.shortcuts import render
#import TodoItem model from models.py
from todo.models import *
def index(request):
    #get all items
    all_items = TodoItem.objects.all()

    return render(request, 'index.html',{'items':all_items})
```
3. Run ``` python manage.py makemigrations``` then ```python manage.py migrate``` which will generate the db script and then migrate will apply to the database
4. To add item to db 
```python
    def add_todo_item(request):
        new_item = TodoItem(text=request.POST['item'])
        new_item.save()
        items = TodoItem.objects.all()
    return render(request, 'index.html',{'items':items, 'errors': errors})
```
5. To delete item to db 
```python
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

```
6. Regex for url with delete ```url(r'^delete-todo-item/(?P<item_id>\d+)$', views.delete_todo_item, name='delete_todo_item'),```

## Add authentication using django's built in  module

1. To INSTALL_APPS of webapps/settings.py add ```django.contrib.auth```
2. Recommended: configure LOGIN_URL and LOGIN_REDIRECT_URL in settings.py file
```python
    #url if login is required
    LOGIN_URL = '/todo/login'
    #default url after user logs in
    LOGIN_REDIRECT_URL = '/todo/'
```
3. Urls add additional routes for login and logout use imported django.contrib.auth. For register use our own
```python
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^add-todo-item$', views.add_todo_item, name='add_todo_item'),
    url(r'^delete-todo-item/(?P<item_id>\d+)$', views.delete_todo_item, name='delete_todo_item'),
    # Route for built-in authentication with our own custom login page. Url dispatcher will send template_name 
    # to the django login function
    url(r'^login$', auth_views.login, {'template_name':'login.html'}, name='login'),
    # Route to logout a user and send them back to the login page
    url(r'^logout$', auth_views.logout_then_login, name='logout'),
    url(r'^register$', views.register, name='register'),
]
```
4. Add user to models
```python
# User class for built-in authentication module
from django.db import models

# User class for built-in authentication module
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
```
5. Actions using django decorator ```@login_required``` to ensure that the user is authenticated or logged in.
```python
#  decorator of django authentication system
from django.contrib.auth.decorators import login_required

.....

.....

@login_required
def home(request):
    # Sets up list of just the logged-in user's items
    items = Item.objects.filter(user=request.user) 
    return render(request, 'index.html', {'items' : items})

```
6. Changes to add_todo_item() and delete_todo_item() actions are 

```python

@login_required
def add_todo_item(request):
   .....
   .....
    else:
        new_item = TodoItem(text=request.POST['item'], user=request.user)
        new_item.save()

    return render(request, 'index.html',{'items':TodoItem.objects.filter(user=request.user), 'errors': errors})

@login_required
def delete_todo_item(request,item_id):
    ...
    ..
        item_to_delete = TodoItem.objects.get(id = item_id, user=request.user)
        item_to_delete.delete()
    ...
    return render(request, 'index.html',context)

```



