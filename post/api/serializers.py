from rest_framework.serializers import ModelSerializer
from post.models import *

class estadoSerializer(ModelSerializer):
    class Meta:
        model = estado
        fields = '__all__'

class categoriaSerializer(ModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'
        
class disponibilidadSerializer(ModelSerializer):
    class Meta:
        model = disponibilidad
        fields = '__all__'

class tipoPublicacionSerializer(ModelSerializer):
    class Meta:
        model = TipoPublicacion
        fields = '__all__'
        
class usuariosSerializer(ModelSerializer):
    class Meta:
        model = usuario
        fields = '__all__'

class productoSerializer(ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__'