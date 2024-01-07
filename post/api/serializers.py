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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UsuariosSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_instance = User.objects.create(**user_data)
        
        usuario_instance = Usuario.objects.create(user=user_instance, **validated_data)
        return usuario_instance

class ProductoSerializer(serializers.ModelSerializer):
    estado_producto = EstadoSerializer()
    categoria = CategoriaSerializer()
    disponibilidad = DisponibilidadSerializer()
    TipoPublicacion = TipoPublicacionSerializer()
    

    class Meta:
        model = Producto
        fields = ['id','nombre_producto','precio_producto','descripcion_producto','estado_producto','categoria','TipoPublicacion','disponibilidad']

class PublicacionSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()
    usuario = UsuariosSerializer()

    class Meta:
        model = Publicacion
        fields = ['id', 'fecha_publicacion', 'producto', 'usuario']

    def get_producto(self, obj):
        return obj.Producto.nombre_producto if obj.Producto else None

    def get_usuario(self, obj):
        return obj.usuario.username if obj.usuario else None



class DetallePublicacionSerializer(serializers.ModelSerializer):
    Producto = ProductoSerializer()
    usuario = UsuariosSerializer()

    class Meta:
        model = Publicacion
        fields = ['fecha_publicacion', 'usuario', 'Producto']