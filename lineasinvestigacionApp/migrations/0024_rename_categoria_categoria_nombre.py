# Generated by Django 3.2.5 on 2021-08-03 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lineasinvestigacionApp', '0023_auto_20210803_0857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='categoria',
            new_name='nombre',
        ),
    ]
