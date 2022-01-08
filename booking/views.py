from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from booking.models import Booking, Invoice, Room
from booking.serializers import BookingSerializer, RoomSerializer, InvoiceSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from booking.utils import get_date

@api_view(['GET'])
def search_rooms(request, start_date, end_date, guests):
    response = {"data":None, "error":None}
    start_date = get_date(start_date, '%d-%m-%Y')
    end_date = get_date(end_date, '%d-%m-%Y')

    if(start_date is None or end_date is None) :
        response["error" ] = {"message":"El formato de las fechas debe ser dd-mm-yyyy"}
        return Response(response, status=400)
    
    queryset =Room.get_rooms_booking(start_date, end_date, guests)
    serializer = RoomSerializer(queryset, many=True)
    response["data"] = serializer.data
    return Response(response)

@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def register_invoice(request):
    response = {"data":None, "error":None}
    data = request.data
    data["user"] = request.user
    invoice_serializer = InvoiceSerializer(data=request.data)
    
    if(invoice_serializer.is_valid()):
        invoice_serializer.save()
        response["data"] = invoice_serializer.data
        return Response(response)
    else:
        response["error"] = {
            "message":"No se pudo registrar", 
            "detail":invoice_serializer.errors
        }
        return Response(data=response,status=400)

@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_booking(request, booking_id):
    response= {"data":None, "error":None}
    try: 
        booking = Booking.objects.get(pk=booking_id)
        booking_serializer = BookingSerializer(booking)
        response["data"] = booking_serializer.data
        return Response(response)
    except ObjectDoesNotExist:
        response["error"] = { "message":"No existe la reserva" }
        return Response(response,404)
        
@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def register_booking(request):
    response = {"data":None, "error":None}
    data = request.data
    data["user"] = request.user
    booking_serializer = BookingSerializer(data=request.data)
    
    if(booking_serializer.is_valid()):
        booking_serializer.save()
        response["data"] = booking_serializer.data
        return Response(response)
    else:
        response["error"] = {
            "message":"No se pudo registrar", 
            "detail":booking_serializer.errors
        }
        return Response(data=response,status=400)

@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_invoice(request, invoice_id):
    
    response = {"data":None, "error":None}
    try: 
        invoice = Invoice.objects.get(pk=invoice_id)
        invoice_serializer = InvoiceSerializer(invoice)
        response["data"] = invoice_serializer.data
        return Response(response)
    except ObjectDoesNotExist:
        response["error"] = { "message":"No existe la factura" }
        return Response(response,404)