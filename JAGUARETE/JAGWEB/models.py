from django.db import models

class Producto (models.Model):
    nombre = models.CharField(max_length=180)
    descripcion = models.CharField(max_length=250)
    categoria = models.CharField(max_length=64)
    precio=models.FloatField()
    imagen=models.CharField(max_length=10)

    def __str__(self):
        return f"Product ID #{self.id}: nombre {self.nombre} desc {self.descripcion} categoria {self.categoria} precio $ {self.precio}"

class Usuario (models.Model):
    nombre=models.CharField(max_length=64)
    apellido=models.CharField(max_length=64)
    correo=models.CharField(max_length=120)

    def __str__(self):
        return f"User ID # {self.id}: {self.nombre} {self.apellido} mail {self.correo} "
