# Generated by Django 3.2 on 2021-05-28 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0072_resultadocanal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Premiacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome da premiação')),
                ('site', models.CharField(blank=True, max_length=100, verbose_name='Link do site')),
                ('desc', models.TextField(blank=True, verbose_name='Descrição da premiação')),
                ('periodo', models.CharField(blank=True, max_length=100, verbose_name='Período de inscrição')),
                ('categorias', models.CharField(max_length=200, verbose_name='Categorias interessantes')),
                ('investimento', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Investimento médio')),
            ],
            options={
                'verbose_name': 'Premiação',
                'verbose_name_plural': 'Premiações',
            },
        ),
    ]