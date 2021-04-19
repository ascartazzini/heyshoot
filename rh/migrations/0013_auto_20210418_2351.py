# Generated by Django 3.2 on 2021-04-18 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0012_auto_20210418_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='status',
        ),
        migrations.AlterField(
            model_name='projeto',
            name='ativismo',
            field=models.IntegerField(blank=True, verbose_name='Ativismo'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='desconto',
            field=models.IntegerField(blank=True, verbose_name='Desconto'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='lucro',
            field=models.IntegerField(blank=True, verbose_name='Lucro'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='valorfinal',
            field=models.IntegerField(blank=True, verbose_name='Valor final'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='valortotal',
            field=models.IntegerField(blank=True, verbose_name='Valor total'),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
