# Generated by Django 3.2.4 on 2021-07-01 14:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('JAGWEB', '0007_auto_20210628_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='fecha',
            field=models.DateTimeField(default=datetime.date(2021, 7, 1)),
        ),
    ]
