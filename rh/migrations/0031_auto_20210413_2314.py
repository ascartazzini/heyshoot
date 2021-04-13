# Generated by Django 3.2 on 2021-04-13 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0030_alter_fornecedores_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='foto',
            field=models.ImageField(blank=True, height_field='foto_y', max_length=600, upload_to='colaboradores/fotos', width_field='foto_x'),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='foto_x',
            field=models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='Foto X'),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='foto_y',
            field=models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='Foto Y'),
        ),
    ]