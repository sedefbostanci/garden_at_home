# Generated by Django 3.0.3 on 2020-08-21 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devicePlants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceplants',
            name='spot_1_Name',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='deviceplants',
            name='spot_2_Name',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='deviceplants',
            name='spot_3_Name',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='deviceplants',
            name='spot_4_Name',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='deviceplants',
            name='spot_5_Name',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='deviceplants',
            name='spot_6_Name',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]
