# Generated by Django 4.0.1 on 2022-01-07 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_room_roomfacility'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='facilities',
            field=models.ManyToManyField(to='booking.RoomFacility'),
        ),
    ]
