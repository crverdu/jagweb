# Generated by Django 3.2.4 on 2021-06-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=180)),
                ('descripcion', models.CharField(max_length=250)),
                ('categoria', models.CharField(max_length=64)),
                ('precio', models.FloatField()),
            ],
        ),
    ]
