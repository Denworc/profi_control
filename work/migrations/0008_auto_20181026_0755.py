# Generated by Django 2.0.5 on 2018-10-26 07:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('work', '0007_auto_20181025_1222'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IncomingСontrol',
            new_name='IncomingControl',
        ),
    ]
