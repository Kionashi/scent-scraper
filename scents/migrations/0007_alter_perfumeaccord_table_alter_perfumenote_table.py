# Generated by Django 4.2.3 on 2023-07-15 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scents', '0006_rename_desginer_perfume_designer'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='perfumeaccord',
            table='scents_perfume_accord',
        ),
        migrations.AlterModelTable(
            name='perfumenote',
            table='scents_perfume_note',
        ),
    ]
