from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
#Hello!

def home(request):
    #return HttpResponse('Hello there friend!')

    #you don't have to specify the templates folder, it apparently looks for it already:
    return render(request, 'generator/home.html', {'password': 'hola123'})

def password(request):
    characters = list('abcdefghijkmnlopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKMLNOPQRSTUVWXYZ')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*')
    if request.GET.get('numbers'):
        characters.extend('1234567890')

    length = int(request.GET.get('length',12)) #with request you can access information provided in the templates (html), with their specific names
                                            #if it is provided by the <form action = 'url'...>
                                            # 12 is default value if no other is provided
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')
