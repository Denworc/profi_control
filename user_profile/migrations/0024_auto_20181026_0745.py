# Generated by Django 2.0.5 on 2018-10-26 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0023_auto_20181023_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='level',
            field=models.CharField(max_length=40, verbose_name='Рівень'),
        ),
    ]