# Serializers are used to turn python objects into JSON objects and only then we can return them as a result in our api calls
from dataclasses import field
from statistics import mode
from rest_framework.serializers import ModelSerializer
from MyApp.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'