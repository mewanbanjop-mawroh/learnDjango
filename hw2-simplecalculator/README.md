#Home work 2

## Django version

Version 1.9.1

##Learnings
1. To make the calculator application's route the default route (localhost:8000) use ```url(r'', include('app_name.urls')),``` as a regex pattern in webapps/urls.py 
2. To including static resources like css, js or images create a folder with the name 'static' in the application folder and put your resources there. You can include it in your templates by add /static/path_to_resource.
3. Use python standard operators as functions ```import operator```
4. Use rtrim and split to separate comma separated values.
5. Handled exceptions using try and except

##Resources
1. http://grasshopperpebbles.com/django-python/how-to-set-up-a-home-page-with-django/
2. https://docs.djangoproject.com/en/1.9/howto/static-files/
3. http://stackoverflow.com/questions/10780423/python-split-function-avoids-last-empy-space
4. https://docs.python.org/2/library/operator.html
5. https://docs.python.org/2/tutorial/errors.html
6. http://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float-in-python