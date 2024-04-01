# Generated by Django 5.0.3 on 2024-03-30 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=20)),
                ('numero', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('usuario', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=50)),
            ],
        ),
    ]
