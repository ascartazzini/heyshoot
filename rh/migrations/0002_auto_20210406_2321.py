# Generated by Django 3.2 on 2021-04-06 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colaborador',
            options={'ordering': ('nome',), 'verbose_name_plural': 'Colaboradores'},
        ),
        migrations.AddField(
            model_name='colaborador',
            name='eh_negra',
            field=models.BooleanField(db_index=True, default=False, verbose_name='É uma pessoa negra?'),
        ),
    ]
