from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from post.models import *
from post.api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

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
    serializer = DetallePublicacionSerializer(publicaciones, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def DetalleProducto(request):
    productosDetalle = Producto.objects.all()
    serializer = ProductoSerializer(productosDetalle, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def DetalleProducto2(request, id):
    try:
        producto = Producto.objects.get(id=id)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    except Producto.DoesNotExist:
        return Response({"error": "Producto not found"})

class DetallePublicacionView(ListAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = DetallePublicacionSerializer
    
    
@csrf_exempt
@require_POST
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Login successful'})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})

