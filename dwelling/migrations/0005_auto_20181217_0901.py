# Generated by Django 2.0.5 on 2018-12-17 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwelling', '0004_auto_20181026_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dwelling',
            name='address',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Адреса проживання'),
        ),
        migrations.AlterField(
            model_name='dwelling',
            name='landlord_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name="Ім'я орендодавця"),
        ),
        migrations.AlterField(
            model_name='dwelling',
            name='neighbor_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='ПІБ сусіда по кімнаті'),
        ),
    ]