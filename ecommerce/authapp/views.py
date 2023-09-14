from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def signup(request):
    return render(request, "signup.html")


def handleLogin(request):
    return render(request, "login.html")


def handleLogout(request):
    return render(request, "login.html")
