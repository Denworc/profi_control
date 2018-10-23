# Generated by Django 2.0.5 on 2018-10-22 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0019_auto_20181022_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='user_profile.Status'),
        ),
    ]