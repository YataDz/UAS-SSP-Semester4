# Generated by Django 5.0.4 on 2024-07-07 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_barangbeli_jumlah_alter_barangbeli_nomor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barangbeli',
            name='jenis',
        ),
    ]