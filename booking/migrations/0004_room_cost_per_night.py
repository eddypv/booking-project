# Generated by Django 4.0.1 on 2022-01-07 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_room_facilities'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='cost_per_night',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]