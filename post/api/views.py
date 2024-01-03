from rest_framework.viewsets import ModelViewSet
from post.models import *
from post.api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

class EstadoApiViewSet(ModelViewSet):
    serializer_class = EstadoSerializer
    queryset = Estado.objects.all()

class CategoriaApiViewSet(ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()

class DisponibilidadApiViewSet(ModelViewSet):
    serializer_class = DisponibilidadSerializer
    queryset = Disponibilidad.objects.all()

class TipoPublicacionApiViewSet(ModelViewSet):
    serializer_class = TipoPublicacionSerializer
    queryset = TipoPublicacion.objects.all()

class UsuariosApiViewSet(ModelViewSet):
    serializer_class = UsuariosSerializer
    queryset = Usuario.objects.all()

class ProductoApiViewSet(ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

class PublicacionApiViewSet(ModelViewSet):
    serializer_class = PublicacionSerializer
    queryset = Publicacion.objects.all()

class DetallePublicacionViewSet(ModelViewSet):
    serializer_class = DetallePublicacionSerializer
    queryset = Publicacion.objects.all()

@api_view(['GET'])
def DetallePublicacion(request):
    publicaciones = Publicacion.objects.all()
    serializer = PublicacionSerializer(publicaciones, many=True)
    return Response(serializer.data)