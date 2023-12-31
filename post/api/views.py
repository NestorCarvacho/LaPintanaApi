from rest_framework.viewsets import ModelViewSet
from post.models import *
from post.api.serializers import *

class estadoApiViewSet(ModelViewSet):
    serializer_class = estadoSerializer
    queryset = estado.objects.all()

class categoriaApiViewSet(ModelViewSet):
    serializer_class = categoriaSerializer
    queryset = categoria.objects.all()
    
class disponibilidadApiViewSet(ModelViewSet):
    serializer_class = disponibilidadSerializer
    queryset = disponibilidad.objects.all()
    
class tipoPublicacionApiViewSet(ModelViewSet):
    serializer_class = tipoPublicacionSerializer
    queryset = TipoPublicacion.objects.all()

class usuariosApiViewSet(ModelViewSet):
    serializer_class = usuariosSerializer
    queryset = usuario.objects.all()
    
class productoApiViewSet(ModelViewSet):
    serializer_class = productoSerializer
    queryset = producto.objects.all()