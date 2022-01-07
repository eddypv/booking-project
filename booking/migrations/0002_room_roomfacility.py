# Generated by Django 4.0.1 on 2022-01-07 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('guests', models.PositiveSmallIntegerField()),
                ('beds', models.PositiveSmallIntegerField()),
                ('toilets', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomFacility',
            fields=[
                ('cod_facility', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('facility', models.CharField(max_length=100)),
            ],
        ),
    ]
