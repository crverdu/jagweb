from django import forms
from .models import Categoria, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre','descripcion','categoria','precio','imagen')

class AddCategory(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre',)

class RegisterUser(UserCreationForm):
    username = forms.CharField(
        label='Usuario', widget=forms.TextInput(attrs={'class': 'usuario'}), max_length=150, required=True, help_text='Requerido. 150 caracteres o menos. Letras, dígitos y @ /. / + / - / _ solamente.')
    first_name=forms.CharField(
        label='Nombre', widget=forms.TextInput(attrs={'class': 'nombre'}), max_length=30, required=False, help_text='Opcional.')
    last_name=forms.CharField(
        label='Apellido', widget=forms.TextInput(attrs={'class': 'apellido'}), max_length=30, required=False, help_text='Opcional.')
    telefono=forms.CharField(
        label='Telefono', widget=forms.TextInput(attrs={'class': 'telefono'}), max_length=15, required=False, help_text='Opcional.')
    email = forms.EmailField(
        label='Email', widget=forms.TextInput(attrs={'class': 'email'}), max_length=254, required=True, help_text='Se requiere una direccion de email valida.')
    password1=forms.CharField(
        label='Password', widget=forms.PasswordInput(), max_length=30, required=True, help_text='Requerido. Al menos 8 caracteres y no pueden ser todos numeros.')
    password2=forms.CharField(
        label='Repetir Password', widget=forms.PasswordInput(), max_length=30, required=True, help_text='Requerido. Ingrese la misma contraseña que antes, para verificación.')

    class Meta:
        model = User
        fields=['username','first_name','last_name','telefono','email','password1','password2']