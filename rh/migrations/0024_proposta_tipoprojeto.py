# Generated by Django 3.2 on 2021-04-21 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0023_auto_20210421_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposta',
            name='tipoprojeto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rh.tipoprojeto', verbose_name='Tipo'),
        ),
    ]
