# Generated by Django 2.0.5 on 2018-10-26 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0024_auto_20181026_0745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='login',
        ),
    ]
