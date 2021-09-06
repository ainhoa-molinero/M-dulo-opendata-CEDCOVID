# Generated by Django 3.2.5 on 2021-08-03 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineasinvestigacionApp', '0026_auto_20210803_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('nombre', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='archivo',
            name='categoria_archivo',
            field=models.ManyToManyField(blank=True, max_length=500, to='lineasinvestigacionApp.Categoria'),
        ),
    ]
