# Generated by Django 4.1.4 on 2022-12-27 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PdfScrapingApp', '0002_alter_insertdatamodel_observation_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='insertdatamodel',
            name='months',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
