# Generated by Django 2.0.5 on 2018-10-31 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_auto_20181031_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ukrainianpassport',
            name='first_page',
            field=models.ImageField(blank=True, null=True, upload_to='user/ua_first', verbose_name='2 сторінка'),
        ),
        migrations.AlterField(
            model_name='ukrainianpassport',
            name='registration',
            field=models.ImageField(blank=True, null=True, upload_to='user/ua_registration', verbose_name='Прописка'),
        ),
        migrations.AlterField(
            model_name='ukrainianpassport',
            name='second_page',
            field=models.ImageField(blank=True, null=True, upload_to='user/ua_second', verbose_name='3 сторінка'),
        ),
    ]
