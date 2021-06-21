from django.db import models

class Producto (models.Model):
    nombre = models.CharField(max_length=180)
    descripcion = models.CharField(max_length=250)
    categoria = models.CharField(max_length=64)
    precio=models.FloatField()

    def __str__(self):
        return f"Product ID #{self.id}: nombre {self.nombre} desc {self.descripcion} categoria {self.categoria} precio $ {self.precio}"

