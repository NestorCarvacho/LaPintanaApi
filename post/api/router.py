from rest_framework.routers import DefaultRouter
from post.api.views import *

router_estados = DefaultRouter()
router_categoria = DefaultRouter()
router_disponibilidad = DefaultRouter()
router_tipoPublicacion = DefaultRouter()
router_usuarios = DefaultRouter()
router_productos = DefaultRouter()
router_publicaciones = DefaultRouter()
router_detallePublicacion = DefaultRouter()
router_DetallePublicacion = DefaultRouter()

router_estados.register(prefix='estado', basename='estado', viewset=EstadoApiViewSet)
router_categoria.register(prefix='categoria', basename='categoria', viewset=CategoriaApiViewSet)
router_disponibilidad.register(prefix='disponibilidad', basename='disponibilidad', viewset=DisponibilidadApiViewSet)
router_tipoPublicacion.register(prefix='tipoPublicacion', basename='tipoPublicacion', viewset=TipoPublicacionApiViewSet)
router_usuarios.register(prefix='usuarios', basename='usuarios', viewset=UsuariosApiViewSet)
router_productos.register(prefix='productos', basename='productos', viewset=ProductoApiViewSet)
router_publicaciones.register(prefix='publicacion', basename='publicacion', viewset=PublicacionApiViewSet)
router_detallePublicacion.register(prefix='detallePublicacion', basename='publicacion', viewset=DetallePublicacionViewSet)
