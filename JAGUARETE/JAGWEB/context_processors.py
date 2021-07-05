from .models import Categoria


def cat_menu(request):
    categorias = Categoria.objects.all()
    return{
        'list_category': categorias
    }

def importe_total_carrito (request):
    total=0
    if request.user.is_authenticated:
        for key, value in request.session['carrito'].items():
            total=total+(float(value["precio"])*value["cantidad"])
    return {"importe_total_carrito":total}

def cantidad_productos (request):
    cantidad=0
    if request.user.is_authenticated:
        cantidad = len(request.session['carrito'])
    return{"cantidad_productos":cantidad}