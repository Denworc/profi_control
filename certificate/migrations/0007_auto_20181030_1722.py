# Generated by Django 2.0.5 on 2018-10-30 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0006_auto_20181025_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interviewtype',
            name='interview',
        ),
        migrations.AddField(
            model_name='interview',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='interviews', to='certificate.InterviewType'),
            preserve_default=False,
        ),
    ]
