# Generated by Django 4.0.3 on 2022-09-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detaillayanan',
            name='iddetaillayanan',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='layanan',
            name='idlayanan',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paketlayanan',
            name='idpaketlayanan',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pemesanan',
            name='idpemesanan',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
