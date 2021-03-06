# Generated by Django 2.0.5 on 2018-12-17 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwelling', '0005_auto_20181217_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dwelling',
            name='address',
            field=models.CharField(blank=True, default=' ', max_length=40, verbose_name='Адреса проживання'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dwelling',
            name='landlord_name',
            field=models.CharField(blank=True, default=' ', max_length=40, verbose_name="Ім'я орендодавця"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dwelling',
            name='neighbor_name',
            field=models.CharField(blank=True, default=' ', max_length=40, verbose_name='ПІБ сусіда по кімнаті'),
            preserve_default=False,
        ),
    ]
