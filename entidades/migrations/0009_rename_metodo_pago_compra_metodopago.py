# Generated by Django 5.0.6 on 2024-07-17 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0008_metodo_de_pago_alter_compra_metodo_pago'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='metodo_pago',
            new_name='metodoPago',
        ),
    ]
