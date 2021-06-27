from django.http.request import HttpRequest
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
class FormularioProductoView(HttpRequest):

    def add_product(request):
        producto = AddProducto()
        return render(request,"product_add.html",{'form':producto})

    def proc_formulario (request):
        producto = AddProducto(request.POST)
        if producto.is_valid():
            producto.save()
            producto = AddProducto()
        return render(request,"product_add.html",{'form':producto,'mensaje':'Ok'})

    def edit_produc (request,idProd):
        producto = Producto.objects.filter(id=idProd).first()
        form = AddProducto(instance=producto)
        return render(request,"product_edit.html",{'form':form,'producto':producto})

    def upd_produc (request,idProd):
        producto = Producto.objects.get(id = idProd)
        form = AddProducto(request.POST,instance = producto)
        if form.is_valid():
            form.save()
        #producto = Producto.objects.get(id = idProd)
        return render(request, "product.html", {
            'un_producto':Producto.objects.get(id = idProd)
        })