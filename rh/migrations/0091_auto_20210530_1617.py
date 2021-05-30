# Generated by Django 3.2 on 2021-05-30 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0090_processo'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='causas',
            field=models.CharField(blank=True, max_length=200, verbose_name='Causas'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='data_final',
            field=models.DateField(blank=True, null=True, verbose_name='Data Final'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='impacto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rh.impacto', verbose_name='Impacto do job'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='ods',
            field=models.ManyToManyField(blank=True, to='rh.Ods', verbose_name='Ods'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='processo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rh.processo', verbose_name='Etapa do processo'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='urlasana',
            field=models.CharField(blank=True, max_length=100, verbose_name='URL do Projeto no Asana'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='urlbriefing',
            field=models.CharField(blank=True, max_length=200, verbose_name='URL do Briefing'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='urldebriefing',
            field=models.CharField(blank=True, max_length=200, verbose_name='URL do Briefing'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='colaboradores',
            field=models.ManyToManyField(blank=True, to='rh.Colaborador', verbose_name='Equipe de apoio'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='lider_shoot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lider', to='rh.colaborador', verbose_name='Líder'),
        ),
    ]
