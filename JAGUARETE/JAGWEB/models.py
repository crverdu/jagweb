from django.db import models

#clase Producto
class Producto (models.Model):
    nombre = models.CharField(max_length=180) #nombre del producto 180 caracteres max
    descripcion = models.CharField(max_length=250) #descripcion breve del producto 250 caracteres
    categoria = models.CharField(max_length=64) #categoria referenciada
    precio=models.FloatField() #precio del producto en float
    imagen=models.CharField(max_length=10) #imagen del producto

    #obtener el objeto producto
    def __str__(self):
        return f"Product ID #{self.id}:{self.nombre} - {self.descripcion} - {self.categoria} - {self.precio}"

#Clase Categoria de productos
class Categoria(models.Model):
    nombre=models.CharField(max_length=64) #Nombre de la categoria

#obtener el objeto Categoria
    def __str__(self):
        return f"Category ID # {self.id}: {self.nombre}"

#Clase Usuario
class Usuario (models.Model):
    nombre=models.CharField(max_length=64) #nombre
    apellido=models.CharField(max_length=64) #Apeliido
    correo=models.CharField(max_length=120) #Correo
    nombreUsuario = models.CharField(max_length=64) #nombre de usuario 64 caracteres

    def __str__(self):
        return f"User ID # {self.id}: {self.nombreUsuario} - {self.nombre} - {self.apellido} - {self.correo} "

#Clase Carrito
class Carrito (models.Model):
    pass
