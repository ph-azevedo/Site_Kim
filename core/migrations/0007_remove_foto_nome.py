# Generated by Django 4.2.1 on 2023-05-23 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_foto_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foto',
            name='nome',
        ),
    ]
