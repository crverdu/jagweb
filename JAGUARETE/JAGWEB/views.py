from django.shortcuts import render,redirect
from .forms import AddProducto
from .models import Producto, Cliente, Categoria
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

def add_product(request):
    if request.method == "POST":
        formulario = AddProducto(request.POST)
        if formulario.is_valid():
            post=formulario.save(commit=True)
            return redirect('product',idProd = post.id)
    else:
        formulario= AddProducto()
    return render(request,"product_add.html",{ 'form':formulario
    })