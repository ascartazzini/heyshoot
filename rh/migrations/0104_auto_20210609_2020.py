# Generated by Django 3.2 on 2021-06-09 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0103_ativismo'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='saiushoot',
            field=models.DateField(blank=True, null=True, verbose_name='Saiu da Shoot dia'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='urldebriefing',
            field=models.CharField(blank=True, max_length=200, verbose_name='URL do Debriefing'),
        ),
    ]