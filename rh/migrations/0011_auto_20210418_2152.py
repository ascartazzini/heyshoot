# Generated by Django 3.2 on 2021-04-18 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0010_projeto_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='ativismo',
            field=models.IntegerField(blank=True, max_length=100, verbose_name='Ativismo'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='desconto',
            field=models.IntegerField(blank=True, max_length=100, verbose_name='Desconto'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='lucro',
            field=models.IntegerField(blank=True, max_length=100, verbose_name='Lucro'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='valorfinal',
            field=models.IntegerField(blank=True, max_length=100, verbose_name='Valor final'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='valortotal',
            field=models.IntegerField(blank=True, max_length=10, verbose_name='Valor total'),
        ),
    ]