from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Usuario, Categoria
# Create your views here.

def index(request):
    return render(request, "index.html",{
        'top3_prod': Producto.objects.all().order_by("-id") [:3],
        'top10_prod': Producto.objects.all().order_by("-id")[3:10]
    })


def about(request):
    return render(request, "about.html")

def searchResoult(request):
    return render(request,"searchResoult.html")

def product(request):
    return render(request,"product.html")