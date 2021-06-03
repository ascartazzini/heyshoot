# Generated by Django 3.2 on 2021-06-02 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0094_financeirotipo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='financeirotipo',
            options={'verbose_name': 'Financeiro | Tipo de Conta', 'verbose_name_plural': 'Financeiro | Tipos de Contas'},
        ),
        migrations.AlterField(
            model_name='financeirotipo',
            name='display',
            field=models.CharField(blank=True, choices=[('e', 'Entrada'), ('s', 'Saída')], max_length=1, null=True, verbose_name='Tipo'),
        ),
        migrations.CreateModel(
            name='FinanceiroGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(blank=True, max_length=200, verbose_name='Nome da conta')),
                ('classifi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rh.financeirotipo', verbose_name='Classificação')),
            ],
            options={
                'verbose_name': 'Financeiro | Conta',
            },
        ),
    ]
