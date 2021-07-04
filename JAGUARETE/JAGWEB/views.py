from django.contrib.auth.models import Group, User
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import AddCategory, AddProducto, RegisterUser
from .models import Producto, Categoria, Carrito, Renglon
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your views here.

#Home de la pagina, sin permisos requeridos
def index(request):
    return render(request, "web/index.html", {
        'top3_prod': Producto.objects.all().order_by("-id")[:3],
        'top10_prod': Producto.objects.all().order_by("-id")[3:10]
    })

#Informacion de la empresa, sin permisos requeridos
def about(request):
    return render(request, "web/about.html")

#Busqueda por categoria, sin permisos requeridos
def search_category(request, id_category):
    return render(request, "producto/searchResoult.html", {
        'una_categoria': Categoria.objects.get(id=id_category),
        'lst_productos': Producto.objects.filter(categoria=id_category)
    })

#busqueda por coincidencia
def busqueda (request):
    query = request.GET.get('buscar', '')
    if query:
        qset = ( 
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query)
        )
        lst_productos=Producto.objects.filter(qset).distinct()
    else:
        lst_productos = []
    return render(request,'producto/searchResoult.html',{
        'lst_productos':lst_productos
    })

#Vista del producto, sin permisos requeridos.
def product(request, idProd):
    return render(request, "producto/product.html", {
        'un_producto': Producto.objects.get(id=idProd)
    })


# Clase para registrar usuarios
class RegistroUsuario (CreateView):
    model = User
    template_name='registration/register.html'
    form_class = RegisterUser
    success_url = reverse_lazy('login')

    #Asignar el rol de usuario comun (cliente) al usuario recien creado.
    @receiver(post_save, sender=User)
    def add_group(sender, instance, created, **kwargs):
        if created:
            group = Group.objects.get(name='comun')
            instance.groups.add(group)

#Crear y asociar carrito al usuario recien registrado.
@receiver(post_save, sender=User)
def add_cart(sender, instance, created, **kwargs):
        if created:
            Carrito.objects.create(cliente=instance)

#Listar productos, para vista de moderador
class ListarProducto(ListView):
    model = Producto
    template_name='web/index_staff.html'
    queryset = Producto.objects.all().order_by("-id")

#Agregar un nuevo producto, moderador o root
class AgregarProducto (CreateView):
    model = Producto
    form_class= AddProducto
    template_name='producto/product_add.html'
    success_url = reverse_lazy ('prod_list')

#Update de  producto, moderador o root
class ActualizarProducto (UpdateView):
    model=Producto
    template_name = 'producto/product_edit.html'
    form_class=AddProducto
    success_url = reverse_lazy('prod_list')

#Delete de producto, moderador o root
class EliminarProducto(DeleteView):
    model=Producto
    template_name='producto/product_del.html'
    success_url=reverse_lazy('prod_list')

class AgregarCategoria(CreateView):
    model=Categoria
    form_class=AddCategory
    template_name = 'categoria/category_add.html'
    success_url=reverse_lazy('list_cat')

class EditarCategoria (UpdateView):
    model= Categoria
    template_name = 'categoria/category_upd.html'
    form_class = AddCategory
    success_url=reverse_lazy('list_cat')

class EliminarCategoria(DeleteView):
    model=Categoria
    template_name='categoria/category_del.html'
    success_url=reverse_lazy('list_cat')

#Listar categorias, para vista de moderador
class ListarCategoria(ListView):
    model = Categoria
    template_name='categoria/category_list.html'
    queryset = Categoria.objects.all().order_by("id")

def cartView(request):
    shop = Carrito.objects.get()
    detalle = Renglon.objects.get()
    return render(request,'carrito/cart_list.html',{'carrito':shop,'detalle':detalle
    })