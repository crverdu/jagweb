from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http.request import HttpRequest
from django.shortcuts import render
from .forms import AddProducto, RegisterUser
from .models import Producto, Categoria
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


def index(request):
    return render(request, "web/index.html", {
        'top3_prod': Producto.objects.all().order_by("-id")[:3],
        'top10_prod': Producto.objects.all().order_by("-id")[3:10]
    })


def about(request):
    return render(request, "web/about.html")


def search_category(request, id_category):
    return render(request, "producto/searchResoult.html", {
        'una_categoria': Categoria.objects.get(id=id_category),
        'lst_productos': Producto.objects.filter(categoria=id_category)
    })


def product(request, idProd):
    return render(request, "producto/product.html", {
        'un_producto': Producto.objects.get(id=idProd)
    })

class FormularioUsuarioView(HttpRequest):
    def add_user (request):
        usuario = RegisterUser()
        return render(request,"usuario/register.html",{'form':usuario})
    def save_register(request):
        usuario = RegisterUser(request.POST)
        if usuario.is_valid():
            usuario.save()
            usuario=RegisterUser()
        return render(request,'usuario/register.html',{'form':usuario,'mensaje':'OK'})


class AgregarProducto (CreateView):
    model = Producto
    form_class= AddProducto
    template_name='producto/product_add.html'
    success_url = reverse_lazy ('index')

class ActualizarProducto (UpdateView):
    model=Producto
    template_name = 'producto/product_edit.html'
    form_class=AddProducto
    success_url = reverse_lazy('index')

class EliminarProducto(DeleteView):
    model=Producto
    template_name='producto/product_del.html'
    success_url=reverse_lazy('index')