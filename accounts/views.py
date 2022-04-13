from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def start_page(request):
    return render(request, 'accounts/start_page.html')


def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thanks')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'registration/register_page.html', {'form': form})


def thanks_page(request):
    return render(request, 'accounts/thanks_page.html')

"""""""""""
def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('start_page')
        else:
            return HttpResponse('Bad login creditentials')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
"""""""""""