# Generated by Django 3.2.4 on 2021-07-01 15:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('JAGWEB', '0009_alter_carrito_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
