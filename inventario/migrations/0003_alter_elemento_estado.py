# Generated by Django 4.2.3 on 2023-09-13 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_alter_elemento_disponibilidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elemento',
            name='estado',
            field=models.CharField(choices=[('buen estado', 'Buen estado'), ('mal estado', 'Mal estado'), ('en reparacion', 'En reparación')], default='Buen estado', max_length=15),
        ),
    ]
