# Generated by Django 3.2.5 on 2021-09-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineasinvestigacionApp', '0030_auto_20210816_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineainvestigacion',
            name='visibilidad',
            field=models.CharField(choices=[('publico', 'publico'), ('privado', 'privado')], default='publico', max_length=10),
        ),
    ]
