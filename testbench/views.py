from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
from ast import literal_eval
import os, time

@login_required(login_url='/accounts/login')
def test(request):
    if request.user.is_authenticated:
        username = request.user.username
        context = {}
        return render(request, 'test/test.html', context)

    else:
        context = {}
        return render(request, 'test/test.html', context)
