# Generated by Django 2.0.5 on 2018-09-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0009_auto_20180925_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='personal_id',
            field=models.CharField(blank=True, max_length=10, unique=True, verbose_name='Идентификационный код'),
        ),
    ]
