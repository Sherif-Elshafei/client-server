from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
	#pull data from db
	#transform data
	#send emails
	return HttpResponse("Hello-world")

def say_hello_friend(request):
    return HttpResponse("hello_friend")