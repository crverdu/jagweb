from django.contrib.auth.models import Group, User
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import AddProducto, RegisterUser
from .models import Producto, Categoria
from django.contrib.auth.decorators import login_required, permission_required

from django.db.models.signals import post_save
from django.dispatch import receiver
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



class RegistroUsuario (CreateView):
    model = User
    template_name='registration/register.html'
    form_class = RegisterUser
    success_url = reverse_lazy('login')

    @receiver(post_save, sender=User)
    def add_group(sender, instance, created, **kwargs):
        if created:
            group = Group.objects.get(name='comun')
            instance.groups.add(group)

class ListarProducto(ListView):
    model = Producto
    template_name='web/index_staff.html'
    queryset = Producto.objects.all().order_by("-id")


class AgregarProducto (CreateView):
    model = Producto
    form_class= AddProducto
    template_name='producto/product_add.html'
    success_url = reverse_lazy ('prod_list')

class ActualizarProducto (UpdateView):
    model=Producto
    template_name = 'producto/product_edit.html'
    form_class=AddProducto
    success_url = reverse_lazy('prod_list')

class EliminarProducto(DeleteView):
    model=Producto
    template_name='producto/product_del.html'
    success_url=reverse_lazy('prod_list')