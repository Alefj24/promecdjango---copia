# Generated by Django 5.0.3 on 2024-03-31 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promecapp', '0002_estado_rol_tipopago_tiposervicio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='IDTipo_servicios',
        ),
        migrations.DeleteModel(
            name='TipoServicio',
        ),
    ]
