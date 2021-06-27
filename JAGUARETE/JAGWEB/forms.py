from django import forms
from .models import Producto

class AddProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre','descripcion','categoria','precio','imagen')
