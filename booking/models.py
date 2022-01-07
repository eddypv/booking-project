from django.db import models

class RoomService(models.Model):
  cod_service = models.CharField(max_length=20,primary_key=True)
  service = models.CharField(max_length=100)
