from rest_framework.decorators import api_view
from rest_framework.response import Response
from MyApp.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]

    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    # many=True because we want to serialize all the available data that 'Room.objects.all()' is returning.
    serializer = RoomSerializer(rooms,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request,pk):
    rooms = Room.objects.get(id=pk)
    # many=False because we want to serialize only one specific record
    serializer = RoomSerializer(rooms,many=False)
    return Response(serializer.data)
