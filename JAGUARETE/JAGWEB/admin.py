from django.contrib import admin
from .models import Producto, Cliente, Categoria, Staff, Carrito

# Register your models here.
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Staff)
admin.site.register(Carrito)