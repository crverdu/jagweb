from django.contrib import admin
from .models import Producto,Categoria,Carrito, Renglon

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Carrito)
admin.site.register(Renglon)