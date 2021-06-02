# Generated by Django 3.2 on 2021-05-30 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0088_ods'),
    ]

    operations = [
        migrations.CreateModel(
            name='Impacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updater', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('peso', models.IntegerField(blank=True, verbose_name='Peso')),
            ],
            options={
                'verbose_name_plural': 'Níveis de Impacto',
            },
        ),
    ]