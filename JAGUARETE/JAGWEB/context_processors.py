from .models import Categoria


def cat_menu(request):
    categorias = Categoria.objects.all()
    return{
        'list_category': categorias
    }

