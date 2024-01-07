from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from apilapintana import settings

# Create your models here.  

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class Estado(models.Model):
    descripcion_estado = models.CharField(max_length=80)
    def __str__(self):
        return self.descripcion_estado
    
class Categoria(models.Model):
    descripcion_categoria = models.CharField(max_length=80)
    def __str__(self):
        return self.descripcion_categoria
    
class TipoPublicacion(models.Model):
    descripcion_TipoPublicacion= models.CharField(max_length=80)
    def __str__(self):
        return self.descripcion_TipoPublicacion
    
class Disponibilidad(models.Model):
    descripcion_disponibilidad = models.CharField(max_length=80)
    def __str__(self):
        return self.descripcion_disponibilidad


class Producto(models.Model):
    nombre_producto = models.CharField(max_length=80)
    precio_producto = models.DecimalField(max_digits=10, decimal_places=0)
    descripcion_producto = models.TextField()
    estado_producto = models.ForeignKey('Estado', related_name='productos', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', related_name='productos', on_delete=models.CASCADE)
    TipoPublicacion = models.ForeignKey('TipoPublicacion', related_name='productos', on_delete=models.CASCADE)
    disponibilidad = models.ForeignKey('Disponibilidad', related_name='productos', on_delete=models.CASCADE)
        
    def __str__(self):
        return self.nombre_producto
        
class Publicacion(models.Model):
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    Producto = models.ForeignKey('Producto', related_name='publicaciones', on_delete=models.CASCADE)
    usuario = models.ForeignKey('Usuario', related_name='publicaciones', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.Producto} || {self.usuario}"
