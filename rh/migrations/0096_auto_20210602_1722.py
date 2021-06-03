# Generated by Django 3.2 on 2021-06-02 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0095_auto_20210602_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceiroClassificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tipo', models.CharField(blank=True, choices=[('Entrada', 'Entrada'), ('Saida', 'Saída')], max_length=10, null=True, verbose_name='Essa conta é')),
                ('classificacao', models.CharField(blank=True, max_length=200, verbose_name='Classificação')),
            ],
            options={
                'verbose_name': 'Financeiro | Classificação',
                'verbose_name_plural': 'Financeiro | Classificações',
            },
        ),
        migrations.AlterField(
            model_name='financeirogrupo',
            name='classifi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='FinanceiroTipo', to='rh.financeiroclassificacao', verbose_name='Classificação'),
        ),
        migrations.DeleteModel(
            name='FinanceiroTipo',
        ),
    ]
