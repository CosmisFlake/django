from rest_framework import serializers
from crud.models import *

class JoyeriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joyeria
        fields = (
            'idJoyeria','name','tipo','marca','value','stock','created_at','updated_at'
        )

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = (
            'id','marca'
        )