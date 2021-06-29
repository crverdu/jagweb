from django.db import models
from datetime import datetime    
#Clase Categoria de productos
class Categoria(models.Model):
    nombre=models.CharField(max_length=64) #Nombre de la categoria

    #obtener el objeto Categoria
    def __str__(self):
        return f"Category ID # {self.id}: {self.nombre}"

#clase Producto
class Producto (models.Model):
    nombre = models.CharField(max_length=180) #nombre del producto 180 caracteres max
    descripcion = models.TextField() #descripcion breve del producto 250 caracteres
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name="categ") #categoria referenciada
    precio=models.FloatField() #precio del producto en float
    imagen= models.ImageField(upload_to='products/', default='products/default.png')   #imagen del producto

    #obtener el objeto producto
    def __str__(self):
        return f"Product ID #{self.id}:{self.nombre} - {self.descripcion} - {self.categoria} - {self.precio} - {self.imagen} "

#Clase Carrito
class Carrito (models.Model):
    fecha = models.DateTimeField(default=datetime.now)
    producto = models.ManyToManyField(Producto,blank=True,related_name="prodCarrito")