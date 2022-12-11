from django.shortcuts import render

from django.contrib.auth import authenticate, login

def log_in(request):


    return render(request, 'auth/login.html')


def register(request):


    return render(request, 'auth/register.html')
