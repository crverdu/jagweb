from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

def searchResoult(request):
    return render(request,"searchResoult.html")

def product(request):
    return render(request,"product.html")