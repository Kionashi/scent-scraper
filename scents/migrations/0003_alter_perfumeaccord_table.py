# Generated by Django 4.2.3 on 2023-07-14 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scents', '0002_perfumer_remove_perfume_perfumists_delete_perfumist_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='perfumeaccord',
            table='perfume_accord',
        ),
    ]