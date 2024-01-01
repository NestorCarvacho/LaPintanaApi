from django.contrib import admin
from post.models import *


# Register your models here.

@admin.register(estado)
class estadoAdmin(admin.ModelAdmin):
    list_display = ['descripcion_estado']
    
@admin.register(categoria)
class categoriaAdmin(admin.ModelAdmin):
    list_display = ['descripcion_categoria']
    
@admin.register(TipoPublicacion)
class TipoPublicacionAdmin(admin.ModelAdmin):
    list_display = ['descripcion_TipoPublicacion']
    
@admin.register(disponibilidad)
class disponibilidadAdmin(admin.ModelAdmin):
    list_display = ['descripcion_disponibilidad']
    
@admin.register(usuario)
class usuarioAdmin(admin.ModelAdmin):
    list_display = ['run_usuario',
                    'dv_usuario',
                    'correo_usuario',
                    'telefono_usuario',
                    'telefono_usuario',
                    'direccion_usuario',
                    'primer_nombre_usuario',
                    'apellido_paterno_usuario',
                    'apellido_materno_usuario',
                    'nombre_fantasia_usuario',
                    'contrasena_usuario']

@admin.register(producto)
class productoAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto',
                    'precio_producto',
                    'descripcion_producto',
                    'estado_producto',
                    'categoria',
                    'TipoPublicacion',
                    'disponibilidad']

@admin.register(publicacion)
class publicacionAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'fecha_publicacion',
                    'producto',
                    'usuario']