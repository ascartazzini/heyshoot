# Generated by Django 3.2 on 2021-05-29 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0077_certificacao_quando'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updater', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome da base')),
                ('objetivo', models.TextField(blank=True, null=True, verbose_name='Objetivo da base')),
                ('inscritos', models.IntegerField(blank=True, verbose_name='Inscritos')),
            ],
        ),
        migrations.AlterField(
            model_name='certificacao',
            name='preco',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Investimento'),
        ),
    ]