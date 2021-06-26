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

def search_category(request, id_category):
    return render(request,"searchResoult.html",{
        'una_categoria': Categoria.objects.get(id=id_category),
        'lst_productos': Producto.objects.filter(categoria=id_category)
    })

def product(request, idProd):
    return render(request,"product.html",{
        'un_producto': Producto.objects.get(id=idProd)
    })