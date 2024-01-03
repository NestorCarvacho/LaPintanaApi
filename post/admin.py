from django.contrib import admin
from post.models import *


# Register your models here.

@admin.register(Estado)
class estadoAdmin(admin.ModelAdmin):
    list_display = ['descripcion_estado']
    
@admin.register(Categoria)
class categoriaAdmin(admin.ModelAdmin):
    list_display = ['descripcion_categoria']
    
@admin.register(TipoPublicacion)
class TipoPublicacionAdmin(admin.ModelAdmin):
    list_display = ['descripcion_TipoPublicacion']
    
@admin.register(Disponibilidad)
class disponibilidadAdmin(admin.ModelAdmin):
    list_display = ['descripcion_disponibilidad']
    
@admin.register(Usuario)
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

@admin.register(Producto)
class productoAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto',
                    'precio_producto',
                    'descripcion_producto',
                    'estado_producto',
                    'categoria',
                    'TipoPublicacion',
                    'disponibilidad']

@admin.register(Publicacion)
class publicacionAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'fecha_publicacion',
                    'Producto',
                    'usuario']