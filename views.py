from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#request --> response
#request handler
def say_hello(request):
    #we can: pull data from db, transform data, send email
    #return HttpResponse('Hello World')
    return render(request, 'hello.html', { 'name': 'Elena'})