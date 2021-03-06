from rest_framework import serializers
from booking.models import Booking, Invoice, Room 
from datetime import datetime
from booking.utils import get_date 

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
        user = data.get("user")
        
        if(amount is None ):
            raise serializers.ValidationError({
                'amount': 'El monto es requerido o mayor a cero'
            })
        
        if(name is None or name == "" ):
            raise serializers.ValidationError({
                'name': 'El nombre es requerido'
            })
        if(nit is None or nit == "" ):
            raise serializers.ValidationError({
                'nit': 'El nit es requerido'
            })
        
        if(booking_id is None  ):
            raise serializers.ValidationError({
                'booking_id': 'La habitacion es requerido'
            })
        if(not Booking.objects.filter(id=booking_id).exists()):
            raise serializers.ValidationError({
                'booking_id': 'No existe la reserva'
            })
        #validar si ya se pago la reserva
        if(Invoice.objects.filter(booking__id=booking_id).exists()):
            raise serializers.ValidationError({
                'booking_id': 'Ya se realizo el pago de esta reserva'
            })
        return {
            "amount":amount,
            "name":name,
            "nit":nit,
            "booking_id":booking_id, 
            "user":user
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

class BookingSerializer(serializers.BaseSerializer):

    def to_internal_value(self, data):
        start_date = get_date(data.get("start_date"), '%d-%m-%Y')
        end_date = get_date(data.get("end_date"), '%d-%m-%Y')
        guests = data.get("guests")
        room_id = data.get("room_id")
        amount_paid = data.get("amount_paid")
        state = data.get("state")
        payment_method = data.get("payment_method")
        user = data.get("user")
        if(start_date is None):
            raise serializers.ValidationError({
                'start_date': 'El formato de la fecha de inicio debe ser dd-mm-yyyy'
            })
        
        if(end_date is None):
            raise serializers.ValidationError({
                'end_date': 'El formato de la fecha de fin debe ser dd-mm-yyyy'
            })
        
        if(room_id is None):
            raise serializers.ValidationError({
                'room_id': 'La habitacion es requerida'
            })
        if(guests is None):
            raise serializers.ValidationError({
                'guests': 'El nro de huspedes es requerido'
            })
        if(amount_paid is None):
            raise serializers.ValidationError({
                'amount_paid': 'El monto pagado es requerido'
            })
        
        if(state is None or not state in [Booking.STATE_PENDIENTE,Booking.STATE_PAGADO]):
            raise serializers.ValidationError({
                'state': 'El estado es requerido o los estados validos son %s y %s ' % (Booking.STATE_PENDIENTE,Booking.STATE_PAGADO)
            })
        
        if(payment_method is None or not payment_method in [Booking.PAYMENT_METHOD_PAYPAL, Booking.PAYMENT_METHOD_TARJETA, Booking.PAYMENT_METHOD_EFECTIVO] ):
            raise serializers.ValidationError({
                'payment_method': 'El metodo de pago es requerido o los metodos de pago validos:%s, %s y %s' %(Booking.PAYMENT_METHOD_PAYPAL, Booking.PAYMENT_METHOD_TARJETA, Booking.PAYMENT_METHOD_EFECTIVO)
            })
        if(not Room.objects.filter(id=room_id).exists()):
            raise serializers.ValidationError({
                'room_id': 'No existe la habitacion'
            })

        return {
            "start_date":start_date,
            "end_date": end_date,
            "guests":guests,
            "room_id": room_id,
            "amount_paid":amount_paid, 
            "state" : state,
            "payment_method" :payment_method,
            "user":user
        }
    
    def to_representation(self, instance):
        return {
            "start_date":instance.start_date,
            "end_date": instance.end_date,
            "guests":instance.guests,
            "room_id": instance.room.id,
            "amount_paid":instance.amount_paid, 
            "state" : {
                "code":instance.state,
                "state":instance.get_state_display()
            },
            "payment_method":{
                "code":instance.payment_method,
                "payment_method":instance.get_payment_method_display()
            }
        }
    def create(self, validated_data):
        return Booking.objects.create(**validated_data)
