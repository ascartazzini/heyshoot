# Generated by Django 3.2 on 2021-04-27 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0024_proposta_tipoprojeto'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='resumo',
            field=models.TextField(blank=True, default='', help_text='Este campo é utilizado na apresentação dos detalhes do projeto no nosso site.', verbose_name='Um breve resumo do projeto'),
        ),
    ]
