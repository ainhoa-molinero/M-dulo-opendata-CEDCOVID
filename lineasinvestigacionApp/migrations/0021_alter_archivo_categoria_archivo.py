# Generated by Django 3.2.5 on 2021-08-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineasinvestigacionApp', '0020_alter_archivo_categoria_archivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='categoria_archivo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
