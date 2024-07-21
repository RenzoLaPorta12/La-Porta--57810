# Generated by Django 5.0.6 on 2024-07-19 13:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0014_avatar'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CantidadPasajeros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Freno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Motor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Traccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='automovil',
            options={'ordering': ['modelo', 'marca', 'año'], 'verbose_name': 'Automóvil', 'verbose_name_plural': 'Automóviles'},
        ),
        migrations.RemoveField(
            model_name='automovil',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='automovil',
            name='pasajeros',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='entidades.cantidadpasajeros'),
        ),
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('año', models.CharField(max_length=50)),
                ('precio', models.CharField(max_length=50)),
                ('tipo_freno', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='entidades.freno')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tipo_motor', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='entidades.motor')),
            ],
            options={
                'verbose_name': 'Moto',
                'verbose_name_plural': 'Motos',
                'ordering': ['modelo', 'marca', 'año'],
            },
        ),
        migrations.CreateModel(
            name='Camioneta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('año', models.CharField(max_length=50)),
                ('precio', models.CharField(max_length=50)),
                ('capacidad_carga', models.CharField(max_length=50)),
                ('tipo_cabina', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='entidades.cabina')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('traccion', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='entidades.traccion')),
            ],
            options={
                'verbose_name': 'Camioneta',
                'verbose_name_plural': 'Camionetas',
                'ordering': ['modelo', 'marca', 'año'],
            },
        ),
    ]
