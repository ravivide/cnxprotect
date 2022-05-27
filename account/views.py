from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect


def logout(request):
    auth.logout(request)
    return redirect('/')
