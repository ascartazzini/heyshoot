# Generated by Django 3.2 on 2021-05-16 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0037_alter_colaborador_funcaodobrother'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hierarquia',
            name='salariobase',
        ),
        migrations.AddField(
            model_name='hierarquia',
            name='salariomax',
            field=models.IntegerField(blank=True, null=True, verbose_name='Salário máximo'),
        ),
        migrations.AddField(
            model_name='hierarquia',
            name='salariomin',
            field=models.IntegerField(blank=True, null=True, verbose_name='Salário mínimo'),
        ),
    ]