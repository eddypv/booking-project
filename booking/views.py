from rest_framework.decorators import api_view
from rest_framework.response import Response
from booking.models import Room
from booking.serializers import RoomSerializer, InvoiceSerializer

@api_view(['GET']) 
def hello_word(request):
    return Response({"message":"hello"})

@api_view(['GET'])
def search_rooms(request, start_date, end_date, guests):
    
    queryset =Room.get_rooms_booking(start_date, end_date, guests)
    serializer = RoomSerializer(queryset, many=True)
    return Response(serializer.data )

@api_view(["POST"])
def register_invoice(request):
    response = {"data":None, "error":None}
    invoice_serializer = InvoiceSerializer(data=request.data)
    
    if(invoice_serializer.is_valid()):
        invoice_serializer.save()
        response["data"] = invoice_serializer.data
        return Response(response)
    else:
        response["error"] = invoice_serializer.errors
        return Response(data=response,status=401)