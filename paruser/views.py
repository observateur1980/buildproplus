from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render


def user_login(request, *args, **kwargs):
    return render(request, 'paruser/login.html',)




# Create your views here.
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def profile(request):
    return render(request, 'paruser/profile.html', )
