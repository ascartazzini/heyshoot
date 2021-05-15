# Generated by Django 3.2 on 2021-05-15 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0029_alter_atividadecomercial_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atividadecomercial',
            options={},
        ),
        migrations.RenameField(
            model_name='atividadecomercial',
            old_name='atividade',
            new_name='nome',
        ),
        migrations.RemoveField(
            model_name='fornecedores',
            name='atividade',
        ),
        migrations.AddField(
            model_name='atividadecomercial',
            name='desc',
            field=models.CharField(blank=True, max_length=100, verbose_name='Alguma descrição?'),
        ),
    ]