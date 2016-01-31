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


