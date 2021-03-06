# Generated by Django 2.0.5 on 2018-09-25 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ForeignPassport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=40, verbose_name='Прізвище')),
                ('last_name', models.CharField(max_length=40, verbose_name="Ім'я")),
                ('type', models.CharField(max_length=1, verbose_name='Тип')),
                ('country_code', models.CharField(max_length=10, verbose_name='Код держави')),
                ('authority', models.CharField(max_length=10, verbose_name='Орган, що видав')),
                ('date_of_expiry', models.DateField(verbose_name='Дата закінчення строку дії')),
            ],
            options={
                'verbose_name': 'Закордонний паспорт',
                'verbose_name_plural': 'Закордонні паспорта',
            },
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=2, verbose_name='Серія')),
                ('number', models.CharField(max_length=6, verbose_name='Номер паспорта')),
                ('date_of_issue', models.DateField(verbose_name='Дата видачі')),
            ],
            options={
                'verbose_name': 'Серійний номер',
                'verbose_name_plural': 'Серійні номера',
            },
        ),
        migrations.CreateModel(
            name='UkrainianPassport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=40, verbose_name='Прізвище')),
                ('last_name', models.CharField(max_length=40, verbose_name="Ім'я")),
                ('patronymic', models.CharField(max_length=40, verbose_name='По батькові')),
                ('place_of_issue', models.CharField(max_length=200, verbose_name='Ким був виданий')),
                ('passport', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='documents.Passport')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Паспорт громадянина України',
                'verbose_name_plural': 'Паспорта громадян України',
            },
        ),
        migrations.AddField(
            model_name='foreignpassport',
            name='passport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.Passport'),
        ),
        migrations.AddField(
            model_name='foreignpassport',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
