# Generated by Django 5.0.4 on 2024-07-07 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barangbeli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodeworld', models.CharField(max_length=10)),
                ('nama', models.CharField(max_length=50)),
                ('growid', models.CharField(max_length=8)),
                ('nomor', models.IntegerField()),
                ('jumlah', models.IntegerField()),
                ('jenis', models.CharField(choices=[('Dana', 'Dana'), ('Shoope Pay', 'Shoope Pay'), ('Ovo', 'Ovo')], default='Dana', max_length=20)),
            ],
        ),
    ]
