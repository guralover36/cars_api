# Generated by Django 5.0.6 on 2024-06-27 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_fuel_type_alter_car_sale_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Brand', 'verbose_name_plural': 'Brands'},
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Car', 'verbose_name_plural': 'Cars'},
        ),
        migrations.AlterModelOptions(
            name='marka',
            options={'verbose_name': 'Marka', 'verbose_name_plural': 'Markas'},
        ),
    ]
