# Generated by Django 5.0.6 on 2024-07-17 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0009_rename_metodo_pago_compra_metodopago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='metodoPago',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='entidades.metodo_de_pago'),
        ),
    ]
