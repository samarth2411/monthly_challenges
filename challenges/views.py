from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def jan(request):
    return HttpResponse("Jan works!!")


def feb(request):
    return HttpResponse("Feb Works!!")
