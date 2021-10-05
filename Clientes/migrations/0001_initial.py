# Generated by Django 3.2.5 on 2021-09-06 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombres', models.CharField(max_length=100)),
                ('Apellidos', models.CharField(max_length=100)),
                ('Direccion', models.CharField(max_length=100)),
                ('Telefono', models.IntegerField(max_length=10)),
                ('Correo', models.EmailField(max_length=254)),
                ('Cedula', models.IntegerField(max_length=10)),
                ('Fecha_Nacimiento', models.DateField()),
            ],
        ),
    ]
