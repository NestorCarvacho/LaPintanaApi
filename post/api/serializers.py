from rest_framework import serializers
from post.models import *

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class DisponibilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibilidad
        fields = '__all__'

class TipoPublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPublicacion
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    estado = serializers.SerializerMethodField()
    categoria = serializers.SerializerMethodField()
    disponibilidad = serializers.SerializerMethodField()
    tipoPublicacion = serializers.SerializerMethodField()
    

    class Meta:
        model = Producto
        fields = ['id','nombre_producto','precio_producto','descripcion_producto','estado','categoria','tipoPublicacion','disponibilidad']

    def get_producto(self, obj):
        return obj.Producto.nombre_producto if obj.Producto else None

    def get_usuario(self, obj):
        return obj.usuario.nombre_fantasia_usuario if obj.usuario else None

    def get_estado(self, obj):
        return obj.estado_producto.descripcion_estado if obj.estado_producto else None

    def get_categoria(self, obj):
        return obj.categoria.descripcion_categoria if obj.categoria else None

    def get_tipoPublicacion(self, obj):
        return obj.TipoPublicacion.descripcion_TipoPublicacion if obj.TipoPublicacion else None

    def get_disponibilidad(self, obj):
        return obj.disponibilidad.descripcion_disponibilidad if obj.disponibilidad else None


class PublicacionSerializer(serializers.ModelSerializer):
    producto = serializers.SerializerMethodField()
    usuario = serializers.SerializerMethodField()

    class Meta:
        model = Publicacion
        fields = ['id', 'fecha_publicacion', 'producto', 'usuario']

    def get_producto(self, obj):
        return obj.Producto.nombre_producto if obj.Producto else None

    def get_usuario(self, obj):
        return obj.usuario.nombre_fantasia_usuario if obj.usuario else None



class DetallePublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'