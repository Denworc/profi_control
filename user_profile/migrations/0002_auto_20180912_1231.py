# Generated by Django 2.0.5 on 2018-09-12 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='patronymic',
            field=models.CharField(max_length=40, verbose_name='Отчество'),
        ),
    ]
