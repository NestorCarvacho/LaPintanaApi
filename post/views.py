from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import producto

def detalle_producto(request, producto_id):
    # Obtén el objeto Producto o devuelve un 404 si no existe
    producto_obj = get_object_or_404(producto, id=producto_id)
    
    # Obtén la representación del producto como un diccionario
    producto_dict = producto_obj.to_dict()
    
    # Devuelve la respuesta JSON
    return JsonResponse(producto_dict)
