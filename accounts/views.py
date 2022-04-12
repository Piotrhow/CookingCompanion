from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from django.contrib.auth.forms import UserCreationForm


def start_page(request):
    return render(request, 'accounts/start_page.html')


def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('thanks')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register_page.html', {'form': form})


def thanks_page(request):
    return render(request, 'accounts/thanks_page.html')


def login_page(request):
    return render(request, 'accounts/login_page.html')
