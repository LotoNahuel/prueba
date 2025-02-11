# Generated by Django 4.1.7 on 2023-04-27 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0007_alter_modelo_diseño'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='diseño',
            field=models.CharField(choices=[('arte', 'Arte'), ('moda', 'Moda'), ('joya', 'Joya'), ('casa', 'Casa'), ('arquitectura', 'Arquitectura'), ('artilugio', 'Artilugio'), ('juego', 'Juego'), ('herramienta', 'Herramienta'), ('otro', 'Otro')], max_length=20),
        ),
    ]
