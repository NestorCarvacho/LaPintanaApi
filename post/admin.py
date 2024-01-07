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
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_usuario', 'numero_telefono', 'correo_electronico', 'nombre_completo', 'usuario']

    def nombre_usuario(self, obj):
        return obj.user.username

    def numero_telefono(self, obj):
        return obj.phone_number

    def correo_electronico(self, obj):
        return obj.user.email

    def nombre_completo(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    def usuario(self, obj):
        return obj.user

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