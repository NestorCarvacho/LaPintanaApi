from django.db import models

# Create your models here.  
class estado(models.Model):
    descripcion_estado = models.CharField(max_length=80)
    def __str__(self):
        return self.descripcion_estado
    
class categoria(models.Model):
    descripcion_categoria = models.CharField(max_length=80)
    def __str__(self):
        return self.descripcion_categoria
    
class TipoPublicacion(models.Model):
    descripcion_TipoPublicacion= models.CharField(max_length=80)
    def __str__(self):
        return self.descripcion_TipoPublicacion
    
class disponibilidad(models.Model):
    descripcion_disponibilidad = models.CharField(max_length=80)
    def __str__(self):
        return self.descripcion_disponibilidad
    
class usuario(models.Model):
    run_usuario = models.IntegerField()
    dv_usuario = models.CharField(max_length=1)
    correo_usuario = models.CharField(max_length=80)
    telefono_usuario = models.IntegerField()
    direccion_usuario = models.CharField(max_length=150)
    primer_nombre_usuario = models.CharField(max_length=80)
    apellido_paterno_usuario = models.CharField(max_length=80)
    apellido_materno_usuario = models.CharField(max_length=80)
    nombre_fantasia_usuario = models.CharField(max_length=80)
    contrasena_usuario = models.CharField(max_length=80)

class producto(models.Model):
    nombre_producto = models.CharField(max_length=80)
    precio_producto = models.IntegerField()
    descripcion_producto = models.TextField()
    estado_producto = models.ForeignKey('Estado', related_name='productos', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', related_name='productos', on_delete=models.CASCADE)
    TipoPublicacion = models.ForeignKey('TipoPublicacion', related_name='productos', on_delete=models.CASCADE)
    disponibilidad = models.ForeignKey('Disponibilidad', related_name='productos', on_delete=models.CASCADE)
        
    def __str__(self):
        return self.nombre_producto + self.descripcion_estado
        print(self.descripcion_estado)