from django.db import models
from django.db.models.base import Model

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
  toilets = models.PositiveSmallIntegerField() #cantidad camas
  facilities = models.ManyToManyField(RoomFacility) 

    




