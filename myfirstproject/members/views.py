from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Welcome to the Members Page!")

# Create your views here.
