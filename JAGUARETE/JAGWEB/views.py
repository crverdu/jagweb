from django.contrib.auth.models import Group, User
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from .forms import AddCategory, AddProducto, RegisterUser
from .models import Producto, Categoria
from django.db.models import Q
from .carrito import Carrito
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your views here.

#Home de la pagina, sin permisos requeridos
def index(request):
    carrito = Carrito(request)
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


#Listar productos, para vista de moderador
class ListarProducto(PermissionRequiredMixin,ListView):
    permission_required = ('JAGWEB.change_producto', 'JAGWEB.view_producto')
    model = Producto
    template_name='web/index_staff.html'
    queryset = Producto.objects.all().order_by("-id")

#Agregar un nuevo producto, moderador o root
class AgregarProducto (PermissionRequiredMixin,CreateView):
    permission_required = 'JAGWEB.add_producto'
    model = Producto
    form_class= AddProducto
    template_name='producto/product_add.html'
    success_url = reverse_lazy ('prod_list')

#Update de  producto, moderador o root
class ActualizarProducto (PermissionRequiredMixin,UpdateView):
    permission_required = 'JAGWEB.change_producto'
    model=Producto
    template_name = 'producto/product_edit.html'
    form_class=AddProducto
    success_url = reverse_lazy('prod_list')

#Delete de producto, moderador o root
class EliminarProducto(PermissionRequiredMixin,DeleteView):
    permission_required = 'JAGWEB.delete_producto'
    model=Producto
    template_name='producto/product_del.html'
    success_url=reverse_lazy('prod_list')

#Agregar categorias, para vista de moderador
class AgregarCategoria(PermissionRequiredMixin,CreateView):
    permission_required ='JAGWEB.add_categoria'
    model=Categoria
    form_class=AddCategory
    template_name = 'categoria/category_add.html'
    success_url=reverse_lazy('list_cat')

#Editar categorias, para vista de moderador
class EditarCategoria (PermissionRequiredMixin,UpdateView):
    permission_required = 'JAGWEB.change_categoria'
    model= Categoria
    template_name = 'categoria/category_upd.html'
    form_class = AddCategory
    success_url=reverse_lazy('list_cat')

#Eliminar categorias, para vista de moderador
class EliminarCategoria(PermissionRequiredMixin,DeleteView):
    permission_required = 'JAGWEB.delete_categoria'
    model=Categoria
    template_name='categoria/category_del.html'
    success_url=reverse_lazy('list_cat')

#Listar categorias, para vista de moderador
class ListarCategoria(PermissionRequiredMixin,ListView):
    permission_required = ('JAGWEB.view_categoria','JAGWEB.add_categoria')
    model = Categoria
    template_name='categoria/category_list.html'
    queryset = Categoria.objects.all().order_by("id")

@login_required
@permission_required('JAGWEB.add_carrito') 
def cart_add_prod (request,id_prod):
    carrito = Carrito(request)
    un_prod = Producto.objects.get(id=id_prod)
    carrito.agregarProd(producto=un_prod)
    return redirect ("index")

@login_required
@permission_required('JAGWEB.add_carrito') 
def cart_sum_prod (request,id_prod):
    carrito = Carrito(request)
    un_prod = Producto.objects.get(id=id_prod)
    carrito.agregarProd(producto=un_prod)
    return redirect ('cart_view')

@login_required
@permission_required('JAGWEB.delete_carrito') 
def cart_del_prod (request,id_prod):
    carrito = Carrito(request)
    un_prod = Producto.objects.get(id=id_prod)
    carrito.eliminarProd(producto=un_prod)
    return redirect ('cart_view')

@login_required
@permission_required('JAGWEB.delete_carrito') 
def cart_rest_prod (request,id_prod):
    carrito = Carrito(request)
    un_prod = Producto.objects.get(id=id_prod)
    carrito.restar_prod(producto=un_prod)
    return redirect ('cart_view')

@login_required
@permission_required('JAGWEB.delete_carrito') 
def limpiar_carrito (request):
    carrito = Carrito(request)
    carrito.limpiar_carrito()
    return redirect ('cart_view')

@login_required
@permission_required('JAGWEB.view_carrito') 
def carrito_view(request):
    return render(request,'carrito/carrito.html')