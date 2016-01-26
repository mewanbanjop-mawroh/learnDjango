#Learning Python and Django

## Installation and Creating new project
1. Install [python] (https://www.python.org/download/), [pip] (https://pip.pypa.io/en/stable/) and in the terminal type `pip install Django`

2.Create a new django project 
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

a. settings.py 
	..* which contain the project settings.
	..* add your new application to the INSTALLED_APPS configuration
b. urls.py 
	..* default configuration for routing Http requests.
	..* add regex rule for your application route "url(r'^application_name/', application_name.urls),". The first parameter is the regex rule and the second is the location which is application_name/urls.py
	```python
			from django.conf.urls import url
		from django.contrib import admin

		urlpatterns = [
		    url(r'^admin/', admin.site.urls),
		    url(r'^application_name/', application_name.urls),
		]
	```

## Create your application routes 
	
	a. Create a new file application_name/urls.py
	b. add the route for your actions e.g.
	
	```python
	from django.conf.urls import url
	from django.contrib import admin

	urlpatterns = [
	    url(r'^hello-world$', 'application_name.views.hello_world'),
	]
	```



