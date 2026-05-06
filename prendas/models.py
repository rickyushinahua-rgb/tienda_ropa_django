from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='categorias/')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Prenda(models.Model):
    nombre = models.CharField(max_length=100)
    talla = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='prendas/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre