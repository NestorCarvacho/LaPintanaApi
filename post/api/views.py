from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from post.models import *
from post.api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

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
    
    
@permission_classes([AllowAny])
class RegisterUser(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            return Response({'error': 'Provide username, password, and email.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        # Additional logic for user creation

        return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)

class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh_token = response.data['refresh']
        access_token = response.data['access']

        user = self.user
        return Response({
            'user_id': user.id,
            'username': user.username,
            'access_token': access_token,
            'refresh_token': refresh_token,
        })