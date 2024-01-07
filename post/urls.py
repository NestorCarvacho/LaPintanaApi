from django.urls import path, include
from rest_framework import routers
from post.api.views import *
from post.api.serializers import *

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('estado', EstadoApiViewSet)
router.register('categoria', CategoriaApiViewSet)
router.register('disponibilidad', DisponibilidadApiViewSet)
router.register('tipoPublicacion', TipoPublicacionApiViewSet)
router.register('usuarios', UsuariosApiViewSet)
router.register('productos', ProductoApiViewSet)
router.register('publicaciones', PublicacionApiViewSet)
router.register('detallePublicacion', DetallePublicacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('detallePublicacionProducto', DetallePublicacion, name='detallePublicacionProducto'),
    path('detalleProducto', DetalleProducto, name='detalleProducto'),
    path('detalleProducto/<int:id>', DetalleProducto2, name='detalleProducto'),
    path('detalle-publicacion/', DetallePublicacionView.as_view(), name='detalle_publicacion'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
