# Generated by Django 3.2 on 2021-05-15 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0027_auto_20210515_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtividadeComercial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('atividade', models.CharField(blank=True, max_length=100, verbose_name='Qual a atividade Comercial')),
            ],
        ),
        migrations.AddField(
            model_name='fornecedores',
            name='atividade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rh.atividadecomercial', verbose_name='Atividade Comercial?'),
        ),
    ]
