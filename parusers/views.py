from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
