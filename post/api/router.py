from rest_framework.routers import DefaultRouter
from post.api.views import *

router_estados = DefaultRouter()
router_categoria = DefaultRouter()
router_disponibilidad = DefaultRouter()
router_tipoPublicacion = DefaultRouter()
router_usuarios = DefaultRouter()
router_productos = DefaultRouter()

router_estados.register(prefix='estado', basename='estado', viewset=estadoApiViewSet)
router_categoria.register(prefix='categoria', basename='categoria', viewset=categoriaApiViewSet)
router_disponibilidad.register(prefix='disponibilidad', basename='disponibilidad', viewset=disponibilidadApiViewSet)
router_tipoPublicacion.register(prefix='tipoPublicacion', basename='tipoPublicacion', viewset=tipoPublicacionApiViewSet)
router_usuarios.register(prefix='usuarios', basename='usuarios', viewset=usuariosApiViewSet)
router_productos.register(prefix='productos', basename='productos', viewset=productoApiViewSet)