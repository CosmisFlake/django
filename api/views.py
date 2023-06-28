from django.shortcuts import render, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from crud.models import *
from .serializers import *

# Create your views here.
@api_view(['GET','POST','DELETE'])
def joyeria_lista(request):
    if request.method == 'GET':
        joyerias = Joyeria.objects.all()
        joyerias_serializer = JoyeriaSerializer(joyerias,many=True)
        return Response(joyerias_serializer.data)
    
    elif request.method == 'POST':
        joyeria_data = JSONParser().parse(request)
        joyeria_serializer = JoyeriaSerializer(data=joyeria_data)
        if joyeria_serializer.is_valid():
            joyeria_serializer.save()
            return Response(joyeria_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(joyeria_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cantidad = Joyeria.objects.all().delete()
        return Response({'mensaje':'Se han eliminado {} tipos de joyeria de la base de datos.'.format(cantidad[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def joyeria_detail(request, joyeria_id):
    try:
        joyeria = Joyeria.objects.get(idJoyeria=joyeria_id)
    except:
        return Response({'mensaje':'La joyeria {} no existe en nuestros registros.'.format(joyeria_id)},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        joyeria_serializer = JoyeriaSerializer(joyeria)
        return Response(joyeria_serializer.data)
    
    elif request.method == 'PUT':
        joyeria_data = JSONParser().parse(request)
        joyeria_serializer = JoyeriaSerializer(joyeria,data=joyeria_data)
        if joyeria_serializer.is_valid():
            joyeria_serializer.save()
            return Response(joyeria_serializer.data,status=status.HTTP_202_ACEPTED)
        else:
            return Response(joyeria_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        joyeria.delete()
        return Response({'mensaje':'La Joyeria {} ha sido eliminada de la base de datos'.format(joyeria_id)},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def marcas_lista(request):
    if request.method == 'GET':
        marcas = Marca.objects.all()
        marcas_serializer = MarcaSerializer(marca,many=True)
        return Response(marcas_serializer.data)

    elif request.method == 'POST':
        marca_data = JSONParser().parse(request)
        marca_serializer = MarcaSerializer(data=marca_data)
        if marca_serializer.is_valid():
            marca_serializer.save()
            return Response(marca_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(marca_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
from django.shortcuts import render

# Create your views here.
