from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre','descripcion','categoria','precio','imagen')

class RegisterUser(UserCreationForm):
    nombre=forms.CharField(max_length=64)
    apellido=forms.CharField(max_length=64)
    telefono=forms.CharField(max_length=15)
    email = forms.EmailField()
    password1=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmar Password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=['nombre','apellido','telefono','email','username','password1','password2']
        help_text = {k:"" for k in fields }