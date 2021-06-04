# Generated by Django 3.2 on 2021-06-03 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0098_auto_20210603_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceiroTotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tipo', models.CharField(blank=True, choices=[('Entrada', 'Entrada'), ('Saida', 'Saída')], max_length=20, null=True, verbose_name='Essa conta é')),
                ('categoria', models.CharField(blank=True, choices=[('Receitas Vendas', 'Receitas Vendas'), ('Receitas Financeiras', 'Receitas Financeiras'), ('Despesas Pessoal', 'Despesas Pessoal'), ('Despesas Financeiras', 'Despesas Financeiras'), ('Despesas Gerais', 'Despesas Gerais'), ('Marketing', 'Marketing'), ('Terceiros', 'Serviços de Terceiros'), ('Simples Nacional', 'Simples Nacional'), ('Investimentos', 'Investimentos')], max_length=20, null=True, verbose_name='Qual categoria')),
                ('classifica', models.CharField(blank=True, choices=[('Salário', 'Salário'), ('Prolabore', 'Prolabore'), ('Lucro', 'Lucro'), ('FGTS', 'FGTS'), ('INSS', 'INSS'), ('Demissoes', 'Demissões'), ('Recisoes', 'Recisões'), ('Beneficios', 'Beneficios'), ('Mídia', 'Mídia'), ('Bonus', 'Bonus')], max_length=20, null=True, verbose_name='Classificação da conta')),
                ('outro', models.CharField(blank=True, max_length=100, null=True, verbose_name='É outro fornecedor')),
                ('data', models.DateField(blank=True, null=True, verbose_name='Que dia')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Alguma descrição')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Valor')),
                ('colabo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rh.colaborador', verbose_name='É pra algum colaborador?')),
                ('contashoot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rh.financeirocontashoot', verbose_name='Qual conta será usada')),
                ('proposta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rh.proposta', verbose_name='É sobre alguma proposta?')),
            ],
            options={
                'verbose_name': 'Financeiro',
            },
        ),
        migrations.RemoveField(
            model_name='financeiroentrada',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='financeiroentrada',
            name='contashoot',
        ),
        migrations.RemoveField(
            model_name='financeiroentrada',
            name='grupo',
        ),
        migrations.RemoveField(
            model_name='financeirogrupo',
            name='classifi',
        ),
        migrations.RemoveField(
            model_name='financeirosaida',
            name='contashoot',
        ),
        migrations.RemoveField(
            model_name='financeirosaida',
            name='grupo',
        ),
        migrations.RemoveField(
            model_name='financeirosaidasalario',
            name='colab',
        ),
        migrations.RemoveField(
            model_name='financeirosaidasalario',
            name='contashoot',
        ),
        migrations.RemoveField(
            model_name='financeirosaidasalario',
            name='grupo',
        ),
        migrations.DeleteModel(
            name='FinanceiroClassificacao',
        ),
        migrations.DeleteModel(
            name='FinanceiroEntrada',
        ),
        migrations.DeleteModel(
            name='FinanceiroGrupo',
        ),
        migrations.DeleteModel(
            name='FinanceiroSaida',
        ),
        migrations.DeleteModel(
            name='FinanceiroSaidaSalario',
        ),
    ]