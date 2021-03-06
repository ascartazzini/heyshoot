# Generated by Django 3.2 on 2021-05-29 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0075_inscricao_quando'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(blank=True, max_length=150, verbose_name='Nome da certificação')),
                ('selo_x', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='Selo X')),
                ('selo_y', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='Selo Y')),
                ('selo', models.ImageField(blank=True, height_field='selo_y', max_length=600, upload_to='certificacoes/logos', width_field='selo_x')),
                ('desc', models.TextField(blank=True, verbose_name='Descrição da certificação')),
                ('preco', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Investimento')),
            ],
            options={
                'verbose_name': 'Certificação',
                'verbose_name_plural': 'Certificações',
            },
        ),
    ]
