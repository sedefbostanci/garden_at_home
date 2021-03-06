# Generated by Django 3.0.3 on 2020-08-21 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devicePlants', '0002_auto_20200821_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceSlots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remaining_Time', models.IntegerField(blank=True, null=True)),
                ('starting_Date', models.CharField(blank=True, max_length=55, null=True)),
                ('plant_Name', models.CharField(blank=True, max_length=55, null=True)),
                ('avg_GrowTime', models.IntegerField(blank=True, null=True)),
                ('plant_Description', models.CharField(blank=True, max_length=255, null=True)),
                ('plant_Tips', models.CharField(blank=True, max_length=255, null=True)),
                ('device_Info', models.CharField(blank=True, max_length=55, null=True)),
                ('devicePlants_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devicePlants.DevicePlants')),
            ],
        ),
    ]
