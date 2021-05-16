# Generated by Django 3.2 on 2021-05-16 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0036_alter_colaborador_funcaodobrother'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='funcaodobrother',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rh.hierarquia', verbose_name='Qual a função atual'),
        ),
    ]