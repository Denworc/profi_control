# Generated by Django 2.0.5 on 2018-10-22 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0018_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='status', to=settings.AUTH_USER_MODEL),
        ),
    ]
