# Generated by Django 4.2.11 on 2024-04-18 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis_ontology', '0035_versionwork_versionplace_versioninstitution_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='pdf_filename',
            field=models.CharField(blank=True),
        ),
    ]
