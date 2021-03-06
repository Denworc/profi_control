# Generated by Django 2.0.5 on 2018-10-26 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('work', '0008_auto_20181026_0755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disappearance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('violation_date', models.DateField(blank=True, null=True, verbose_name='Дата порушення')),
                ('appeal_date', models.DateField(blank=True, null=True, verbose_name='Дата звернення')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='disappearances', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Зникнення',
                'verbose_name_plural': 'Зникнення',
            },
        ),
        migrations.CreateModel(
            name='Prognosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=40, verbose_name='Причина повернення')),
                ('expire', models.DateField(blank=True, null=True, verbose_name='Дата прибуття')),
                ('agree', models.BooleanField(default=False, verbose_name='Згода заводу')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='prognoses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Прогноз',
                'verbose_name_plural': 'Прогнози',
            },
        ),
    ]
