# Generated by Django 2.0.5 on 2018-09-17 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_auto_20180917_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='personal_id',
            field=models.CharField(max_length=10, unique=True, verbose_name='Идентификационный код'),
        ),
    ]
