from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .forms import SignUpForm

# Create your views here.


def user_login(request: HttpRequest) -> HttpRequest:
    return render(request, 'authentication/login.html')


def register(request: HttpRequest) -> HttpRequest:
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("Form errors:", form.errors)
        if form.is_valid():
            form.save()
            return redirect('user_auth:user_login')
    else:
        form = SignUpForm()
    return render(request, 'authentication/register.html', {'form': form})


def authenticate_user(request: HttpRequest) -> HttpRequest:
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('polls:index')
        )


def show_user(request: HttpRequest) -> HttpRequest:
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })
