# Generated by Django 3.2 on 2021-04-21 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0022_tipo_projeto'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoProjeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('descri', models.CharField(blank=True, max_length=600, verbose_name='Descrição')),
                ('tempo', models.IntegerField(blank=True, verbose_name='Tempo do processo')),
            ],
            options={
                'verbose_name': 'Tipo de Projeto',
            },
        ),
        migrations.DeleteModel(
            name='Tipo_projeto',
        ),
    ]
