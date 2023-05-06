from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def login(request):
    return HttpResponse("Hello, world. You're at the polls login.")

@login_required
