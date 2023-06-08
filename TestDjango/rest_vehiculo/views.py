from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Vehiculo, Categoria
from .serializers import VehiculoSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_vehiculos(request):
    """ 
      Listado de todos los vehiculos
    """

    if request.method == 'GET':
        vehiculo = Vehiculo.objects.all()
        serializer = VehiculoSerializer(vehiculo, many=True)
        return Response(serializer.data)