# Generated by Django 3.2 on 2021-05-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0049_auto_20210520_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100, verbose_name='Linkedin'),
        ),
    ]