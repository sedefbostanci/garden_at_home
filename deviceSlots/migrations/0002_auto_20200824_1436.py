# Generated by Django 3.0.3 on 2020-08-24 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deviceSlots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceslots',
            name='plant_Description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deviceslots',
            name='plant_Tips',
            field=models.TextField(blank=True, null=True),
        ),
    ]