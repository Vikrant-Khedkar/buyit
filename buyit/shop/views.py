from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return HttpResponse("In about")


def contact(request):
    return HttpResponse("In contact")


def tracker(request):
    return HttpResponse("In tracker")


def search(request):
    return HttpResponse("In search")


def productView(request):
    return HttpResponse("In productView")


def checkout(request):
    return HttpResponse("In checkout")
