from django.db import models
from django.db.models.base import Model
from django.utils.translation import override

class RoomService(models.Model):
  cod_service = models.CharField(max_length=20, primary_key=True)
  service = models.CharField(max_length=100)

class RoomFacility(models.Model):
  cod_facility = models.CharField(max_length=20, primary_key=True)
  facility = models.CharField(max_length=100)
  

class Room(models.Model):
  title = models.CharField(max_length=200)
  description = models.CharField(max_length=1000)
  guests = models.PositiveSmallIntegerField() # cantidad huspedes
  beds = models.PositiveSmallIntegerField() #cantidad camas
  toilets = models.PositiveSmallIntegerField() #cantidad baños
  facilities = models.ManyToManyField(RoomFacility)  #instalaciones en la habitacion
  cost_per_night = models.DecimalField(max_digits=10, decimal_places=2)
  
  @staticmethod
  def get_rooms_booking(start_date, end_date, guests):
    sentence = """select * 
                from booking_room room 
                where room.guests =%s and not room.id in (
                        select booking.room_id 
                        from booking_booking booking   
                        where (booking.start_date<='%s'  and  booking.end_date>='%s') or 
                        (booking.start_date<='%s'  and  booking.end_date>='%s'))""" %(guests, start_date, start_date, end_date, end_date)
    
    return Room.objects.raw(sentence)


class Booking(models.Model): 
  STATES = (
    ('PEN', 'Pendiente'),
    ('PAG', 'Pagado'),
    ('ELI', 'Eliminado'),
  )
  PAYMENT_METHOD = (
    ('EFEC', 'Pago en Efectivo'),
    ('TAR', 'Pago con Tarjeta de Crédito o Débito'),
    ('PAYP', 'Pago por Paypal'),
  )
  date = models.DateTimeField(auto_now_add=True)
  start_date = models.DateField()
  end_date = models.DateField()
  guests = models.PositiveSmallIntegerField()
  room = models.ForeignKey(Room, on_delete=models.PROTECT)
  amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
  state = models.TextField(max_length=3, choices=STATES)
  payment_method = models.TextField(max_length=4, choices=PAYMENT_METHOD)

class Invoice(models.Model):
  date = models.DateTimeField(auto_now_add=True)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  name = models.TextField(max_length=50)
  nit = models.TextField(max_length=30)
  booking = models.ForeignKey(Booking, on_delete=models.PROTECT)

    




