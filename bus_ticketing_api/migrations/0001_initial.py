# Generated by Django 4.1.3 on 2022-11-14 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('seating_capacity', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Bus',
                'verbose_name_plural': 'Buses',
            },
        ),
        migrations.CreateModel(
            name='BusRoutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('price', models.IntegerField()),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus_ticketing_api.bus')),
            ],
            options={
                'verbose_name': 'Bus Route',
                'verbose_name_plural': 'Bus Routes',
            },
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
            options={
                'verbose_name': 'Place',
                'verbose_name_plural': 'Places',
            },
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('distance', models.IntegerField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='bus_ticketing_api.places')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='bus_ticketing_api.places')),
            ],
            options={
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routes',
            },
        ),
        migrations.CreateModel(
            name='BusSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('bus_route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus_ticketing_api.busroutes')),
            ],
            options={
                'verbose_name': 'Bus Schedule',
                'verbose_name_plural': 'Bus Schedules',
            },
        ),
        migrations.AddField(
            model_name='busroutes',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus_ticketing_api.routes'),
        ),
    ]
