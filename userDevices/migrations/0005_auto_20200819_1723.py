# Generated by Django 3.0.3 on 2020-08-19 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userDevices', '0004_auto_20200819_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdevices',
            name='device_water_level',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
