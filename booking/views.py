from rest_framework.decorators import api_view
from rest_framework.response import Response
from booking.models import Invoice, Room
from booking.serializers import RoomSerializer, InvoiceSerializer
from django.core.exceptions import ObjectDoesNotExist

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
        response["error"] = {
            "message":"No se pudo registrar", 
            "detail":invoice_serializer.errors
        }
        return Response(data=response,status=400)

@api_view(["GET"])
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