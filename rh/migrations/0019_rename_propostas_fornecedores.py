# Generated by Django 3.2 on 2021-04-09 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0018_alter_propostas_cliente'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Propostas',
            new_name='Fornecedores',
        ),
    ]
