# Generated by Django 3.2.4 on 2021-07-04 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JAGWEB', '0012_auto_20210703_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='detalle',
        ),
        migrations.AddField(
            model_name='renglon',
            name='carrito',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='JAGWEB.carrito'),
        ),
    ]
