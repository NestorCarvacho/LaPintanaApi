from django.urls import path, include
from rest_framework import routers
from post.api.views import *
from post.api.serializers import *

router = routers.DefaultRouter()
router.register('estado', estadoApiViewSet)
router.register('categoria', categoriaApiViewSet)
router.register('disponibilidad', disponibilidadApiViewSet)
router.register('tipoPublicacion', tipoPublicacionApiViewSet)
router.register('usuarios', usuariosApiViewSet)
router.register('productos', productoApiViewSet)
router.register('publicaciones', publicacionApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
