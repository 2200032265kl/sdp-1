import csv

from django.contrib.sites import requests
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
import random
import string
# Create your views here.

def hello(request):
    return HttpResponse("<center>Welcome to TTM Homepage</center>")





def newhomepage(request):
    return render(request,'homepage.html')





def travelpackage(request):
    return render(request,'travelpackage.html')


def print1(request):
    return render(request,'print_to_console.html')


def print_to_console(request):
    user_input = ''  # Initialize user_input as an empty string
    if request.method == "POST":
        user_input = request.POST.get('akhila', '')  # Retrieve 'akhila' from POST data or default to empty string
        print(f'User input: {user_input}')

    a1 = {'user_input': user_input}
    return render(request, 'print_to_console.html', a1)

def randomcall(request):
    return render(request,'randomotpgenerator.html')

def randomlogic(request):
    user_input = ''  # Initialize user_input as an empty string
    if request.method == "POST":
        user_input = request.POST.get('akhila', '')  # Retrieve 'akhila' from POST data or default to empty string
        print(f'User input: {user_input}')
        a2=int(user_input)
        ran1 = ''.join(random.sample(string.digits, k=a2))

    a1 = {'ran1': ran1}
    return render(request, 'randomotpgenerator.html', a1)


def getdate1(request):
    return render(request,'get_date.html')

import datetime
from .forms import *
from django.shortcuts import render
def get_date(request):
    if request.method=='POST':
        form=IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value=form.cleaned_data['integer_value']
            date_value=form.cleaned_data['date_value']
            updated_date=date_value+datetime.timedelta(days=integer_value)
            return render(request,'get_date.html',{'updated date':updated_date})
        else:
            form=IntegerDateForm()
        return render(request,'get_date.html',{'form':form})


def migrate111(request):
    return render(request,'migrations123.html')


from .models import Akhila  # Import the Akhila model
from django.shortcuts import render,redirect

def registerloginfunction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')

        if Akhila.objects.filter(email=email).exists():
            return HttpResponse("Email already registered. Choose a different email.")

        # Create Akhila object using variables, not strings
        Akhila.objects.create(name=name, email=email, password=password, phonenumber=phonenumber)

        # Redirect to the 'newhomepage' URL name upon successful registration
        return redirect('newhomepage')

    return render(request, 'migrations123.html')



def weatherpagecall(request):
    return render(request,'weatherappinput.html')


import requests  # Import requests module to make HTTP requests
from django.shortcuts import render  # Import render function from Django

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '92a4c891bb45425480c59bbdc02e3a0b'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1 = round(temperature - 273.15, 2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})

    # Return a response if the request method is not POST
    return render(request, 'weatherappinput.html')


def feedback(request):
    return render(request,'feedback.html')


from .models import Akhilaa  # Import the Akhila model
from django.shortcuts import render,redirect

def feedbacklogic(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        comments = request.POST.get('comments')
        tosend=comments+'this is justa comment'
        data=Akhilaa(firstname=firstname,lastname=lastname,email=email,comments=comments)
        data.save()

        send_mail(
            'Thank you for contacting Akhila traveltourism',
            tosend,
            '2200032265cseh@gmail.com',
            [email],
            fail_silently=False,

        )



    return render(request, 'feedback.html')



from django.shortcuts import render
from django.contrib.auth.models import User ,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'Homepage.html')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def signup1(request):
 if request.method=="POST":
    username=request.POST['username']
    pass1=request.POST['password']
    pass2=request.POST['password1']
    if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Usename already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!!')
                return render(request,'login.html')
    else:
            messages.info(request,'Password do not match')
            return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return render (request,'Homepage.html')


