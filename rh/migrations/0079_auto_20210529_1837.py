# Generated by Django 3.2 on 2021-05-29 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0078_auto_20210529_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='inscritos',
        ),
        migrations.CreateModel(
            name='NewsletterTotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updater', models.DateTimeField(auto_now=True)),
                ('quando', models.DateField(blank=True, null=True, verbose_name='Quando')),
                ('inscritos', models.IntegerField(blank=True, verbose_name='Inscritos')),
                ('news', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rh.newsletter', verbose_name='Base')),
            ],
            options={
                'verbose_name': 'Resultados Newsletter',
            },
        ),
    ]
