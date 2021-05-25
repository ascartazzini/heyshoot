# Generated by Django 3.2 on 2021-05-25 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0053_auto_20210525_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='MomentoImportante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='Nome do momento')),
                ('quando', models.DateField(blank=True, null=True, verbose_name='Data')),
                ('quem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rh.cliente', verbose_name='Pessoa')),
            ],
        ),
    ]
