# Generated by Django 3.2 on 2021-05-30 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0091_auto_20210530_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposta',
            name='urlproposta',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='URL Proposta'),
        ),
    ]
