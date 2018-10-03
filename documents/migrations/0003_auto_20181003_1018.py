# Generated by Django 2.0.5 on 2018-10-03 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documents', '0002_visa'),
    ]

    operations = [
        migrations.CreateModel(
            name='MilitaryRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_on', models.DateField(blank=True, null=True, verbose_name='Дата взяття на облік')),
                ('expire', models.DateField(blank=True, null=True, verbose_name='Дата зняття з обліку')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Військовий облік',
                'verbose_name_plural': 'Військові обліки',
            },
        ),
        migrations.CreateModel(
            name='PersonalID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_id', models.CharField(blank=True, max_length=10, unique=True, verbose_name='Ідентифікаційний код')),
                ('scan_id', models.ImageField(blank=True, null=True, upload_to='user/id', verbose_name='Скан копія')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ідентифікаційний код',
                'verbose_name_plural': 'Ідентифікаційні коди',
            },
        ),
        migrations.RemoveField(
            model_name='foreignpassport',
            name='passport',
        ),
        migrations.RemoveField(
            model_name='ukrainianpassport',
            name='passport',
        ),
        migrations.AddField(
            model_name='foreignpassport',
            name='date_of_issue',
            field=models.DateField(blank=True, null=True, verbose_name='Дата видачі'),
        ),
        migrations.AddField(
            model_name='foreignpassport',
            name='first_page',
            field=models.ImageField(blank=True, null=True, upload_to='user/foreign', verbose_name='1 сторінка'),
        ),
        migrations.AddField(
            model_name='foreignpassport',
            name='number',
            field=models.CharField(default=111111, max_length=6, verbose_name='Номер паспорта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ukrainianpassport',
            name='date_of_issue',
            field=models.DateField(blank=True, null=True, verbose_name='Дата видачі'),
        ),
        migrations.AddField(
            model_name='ukrainianpassport',
            name='first_page',
            field=models.ImageField(blank=True, null=True, upload_to='user/ua_passport', verbose_name='2 сторінка'),
        ),
        migrations.AddField(
            model_name='ukrainianpassport',
            name='number',
            field=models.CharField(default=111111, max_length=6, verbose_name='Номер паспорта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ukrainianpassport',
            name='registration',
            field=models.ImageField(blank=True, null=True, upload_to='user/ua_passport', verbose_name='Прописка'),
        ),
        migrations.AddField(
            model_name='ukrainianpassport',
            name='second_page',
            field=models.ImageField(blank=True, null=True, upload_to='user/ua_passport', verbose_name='3 сторінка'),
        ),
        migrations.AddField(
            model_name='ukrainianpassport',
            name='series',
            field=models.CharField(default='AA', max_length=2, verbose_name='Серія'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visa',
            name='visa_scan',
            field=models.ImageField(blank=True, null=True, upload_to='user/visa', verbose_name='Скан копія'),
        ),
        migrations.AlterField(
            model_name='foreignpassport',
            name='date_of_expiry',
            field=models.DateField(blank=True, null=True, verbose_name='Дата закінчення строку дії'),
        ),
        migrations.AlterField(
            model_name='visa',
            name='expire',
            field=models.DateField(blank=True, null=True, verbose_name='Дата закінчення строку дії'),
        ),
        migrations.AlterField(
            model_name='visa',
            name='start_on',
            field=models.DateField(blank=True, null=True, verbose_name='Дата початку'),
        ),
        migrations.DeleteModel(
            name='Passport',
        ),
    ]
