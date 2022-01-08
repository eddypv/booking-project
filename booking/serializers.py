from rest_framework import serializers

from booking.models import Booking, Invoice 

class RoomFacilitySerializer(serializers.BaseSerializer):
    def to_representation(self,instance):
        return{
            "cod_facility":instance.cod_facility,
            "facility":instance.facility,
        }

class RoomSerializer(serializers.BaseSerializer):
    #JSON
    def to_representation(self,instance):
        
        serializer_facilities = RoomFacilitySerializer(instance.facilities.all(), many=True)
        return {
            "id":instance.id,
            "title":instance.title,
            "description" : instance.description,
            "guests": instance.guests,
            "beds": instance.beds,
            "toilets": instance.toilets,
            "cost_per_night" :instance.cost_per_night,
            "facilities":serializer_facilities.data
        }

class InvoiceSerializer(serializers.BaseSerializer):
    #retornar informacion valida
    def to_internal_value(self, data):
        amount = data.get("amount")
        name = data.get("name")
        nit = data.get("nit")
        booking_id= data.get("booking_id")

        #validar si ya se pago la reserva
        if(Invoice.objects.filter(booking__id=booking_id).exists()):
            raise serializers.ValidationError({
                'booking_id': 'Ya se realizo el pago de esta reserva'
            })
        return {
            "amount":amount,
            "name":name,
            "nit":nit,
            "booking_id":booking_id
        }
    # JSON
    def to_representation(self, instance):
        return {
            "id":instance.id,
            "date": instance.date,
            "amount":instance.amount,
            "name":instance.name,
            "nit":instance.nit,
            "booking_id":instance.booking.id
        }
    
    def create(self, validated_data):
        return Invoice.objects.create(**validated_data)

        