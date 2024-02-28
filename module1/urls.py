from django.contrib import admin
from django.urls import path
from.views import*

urlpatterns = [
    path('hello/',hello,name='hello'),
    path('',newhomepage,name='newhomepage'),
    path('travelpackage/',travelpackage,name='travelpackage'),
    path('print/', print_to_console, name='print_to_console'),
    path('p/',print1,name='print1'),
    path('randomcall/', randomcall, name='randomcall'),
    path('randomlogic/',randomlogic,name='randomlogic'),
    path('getdate1/', getdate1, name='getdate1'),
    path('get_date/', get_date, name='get_date'),
    path('migrate111/', migrate111, name='migrate111'),
    path('registerloginfunction', registerloginfunction, name='registerloginfunction'),
    path('wetherpagecall/', weatherpagecall, name='wetherpagecall'),
    path('weatherlogic/', weatherlogic, name='weatherlogic'),
    path('feedback/', feedback, name='feedback'),
    path('feedbacklogic/', feedbacklogic, name='feedbacklogic'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
]
