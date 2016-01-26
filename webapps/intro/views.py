from django.shortcuts import render

#action for 'intro/hello-world' route
def hello_world(request):
	#render takes (1) the request, 
	#(2) the name of the view to generate and 
	#(3) key-value pair for template views
	return render(request,'hello-world.html',{})

#action for 'intro/hello' route
def hello(request):
	#creates a dictionary for 
	context = {}
	context['person_name'] = ''
	
	#retrieves username from request if available in http get parameter
	if 'username' in request.GET:
		context['person_name'] = request.GET['username']
	return render(request,'intro/views/hello-world.html',{})
