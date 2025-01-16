# Generated by Django 2.2.24 on 2025-01-16 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20250115_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owned_flats',
            field=models.ManyToManyField(related_name='owner_data', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_name',
            field=models.CharField(max_length=200, verbose_name='ФИО владельца'),
        ),
    ]
