# Generated by Django 4.0.1 on 2022-01-07 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_booking_invoce'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Invoce',
            new_name='Invoice',
        ),
    ]