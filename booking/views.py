from rest_framework.decorators import api_view
from rest_framework.response import Response
from booking.models import Room
from booking.serializers import RoomSerializer
@api_view(['GET']) 
def hello_word(request):
    return Response({"message":"hello"})

@api_view(['GET'])
def search_rooms(request, start_date, end_date, guests):
    
    queryset =Room.get_rooms_booking(start_date, end_date, guests)
    serializer = RoomSerializer(queryset, many=True)
    return Response(serializer.data )