from django.shortcuts import render
# importing the operator module which uses standard operators as functions
import operator

#List of operator characters
operatorList = ['+','-','*','/','=']

#dictionary of operator character to operator functions
operations = { '+': operator.add, '-': operator.sub, '/': operator.div, '*': operator.mul }

#Default action of calculator that returns index page
def home(request):
	return render(request,'index.html',createDefaultContext([]))

# Post action for subsequent requests
def calculate(request):
	errors = []
	try:
		req = readValuesFromRequest(request)
	except ValueError as err:
		errors.append(err.message)
		return render(request,'index.html',createDefaultContext(errors))
	
	if operatorIsEntered(req):
		context = processOperator(req,errors)
		return render(request,'index.html',context)
	else:
		context = processDigit(req,errors)
		return render(request,'index.html',context)

def createDefaultContext(errors):
	return createContext(0,'',errors)

def createContext(display,history,errors):
	return {'display': display, 'history':history, 'errors': errors}

def readValuesFromRequest(request):
	operator = request.POST['operator'] if 'operator' in request.POST else ''
	history = request.POST['history']
	digit = request.POST['digit'] if 'digit' in request.POST else ''
	if digit != '' and not digit.isdigit():
		raise ValueError("Wrong input. Not digit")
	if operator != '' and operator not in operatorList:
		 raise ValueError("Wrong input. Not an operator.")
	display = request.POST['display']
	return {'operator' : operator,'history' :history,'digit' :digit,'display' :display }

def performBinaryCalculation(req):
	#split csv to array of 3 elements [firstOperand, operator,secondOperand]
	historyArray = req['history'].rstrip(',').split(',') 
	firstOperand = int(historyArray[0])
	operator = historyArray[1]
	secondOperand = int(historyArray[2])
	return str(operations[operator] (firstOperand,secondOperand))
	
def hasOlderExpressionsToProcess(req):
	#split csv to array of and check if it has 3 elements [firstOperand, operator,secondOperand]
	historyArray = req['history'].rstrip(',').split(',')
	return len(historyArray) == 3

def previousEntryIsAnOperator(req):
	historyArray = req['history'].rstrip(',').split(',') 
	return historyArray[-1] in operatorList

def operatorIsEntered(req):
	return req['operator'] not in [None, '']

def operatorIsTheFirstEntryOfCalculator(req):
	return isHistoryEmpty(req) and isDigitEmpty(req)

def isHistoryEmpty(req):
	return req['history'] in [None,'']

def isDigitEmpty(req):
	return req['digit'] in [None,'']

def processOperator(req,errors):
	#When an operator is entered as the first entry do nothing
	if operatorIsTheFirstEntryOfCalculator(req):
		return createDefaultContext(errors)
	#Check if an operator is the previous entry and replace it
	elif previousEntryIsAnOperator(req):
		#Replace the earlier operator unless the current operator is '='
		if req['operator'] != '=':
			#updating history by replacing the previous operator
			req['history'] = req['history'].replace(req['history'][-2],req['operator']) 
	#Check if there are any older expressions to calcualte
	elif hasOlderExpressionsToProcess(req):
		try:
			result = performBinaryCalculation(req)
		except ZeroDivisionError, e:
			errors.append("Divide by zero")
			return createContext(0,'',errors)
		if req['operator'] == '=':
			req['history'] = ''
		else:
			req['history'] = result + ',' + req['operator'] + ','#updating history with result and appending the operator
		req['display'] = result
		# req['digit'] = ''
	
	else:
		req['history'] += ',' + req['operator'] + ',' #updating history
	#When a value is entered
	return createContext(req['display'],req['history'],errors)

def processDigit(req,errors):
	#rewrite the display with new value when history is empty
	if isHistoryEmpty(req):
		req['display'] = req['digit']
	#rewrite the display with new value after operator
	elif previousEntryIsAnOperator(req):
		req['display'] = req['digit']
	else :
		#overiding display value if previous display value is 0 otherwise append to previous display value
		req['display'] = req['digit'] if req['display'] == '0' else req['display'] + req['digit']
	#append the last integer value
	req['history'] += req['digit']
	return createContext(req['display'],req['history'],errors)


			
	
