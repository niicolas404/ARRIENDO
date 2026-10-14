from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    stock = models.PositiveIntegerField()
    url_imagen = models.URLField(max_length=200)

    def __str__(self):
        return self.nombre
    
class Arriendo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="arriendos")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cliente = models.CharField(max_length=100)
    precio = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cliente} - {self.equipo.nombre}"
    
    def precio_formateado(self):
        return f"${self.precio:,.2f}".replace(",", ".")