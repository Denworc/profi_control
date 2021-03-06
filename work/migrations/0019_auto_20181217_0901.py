# Generated by Django 2.0.5 on 2018-12-17 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0018_auto_20181203_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptioninstate',
            name='dismissal_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата прийняття'),
        ),
        migrations.AlterField(
            model_name='adoptioninstate',
            name='order_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='№ наказу'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='city',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Місто відрядження'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='order_number',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='№ наказу'),
        ),
        migrations.AlterField(
            model_name='dismissal',
            name='dismissal_reason',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Причина звільнення'),
        ),
        migrations.AlterField(
            model_name='dismissal',
            name='order_number',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='№ наказу'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='note',
            field=models.CharField(blank=True, max_length=400, verbose_name='Примітки'),
        ),
        migrations.AlterField(
            model_name='prognosis',
            name='reason',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Причина повернення'),
        ),
        migrations.AlterField(
            model_name='transferinstate',
            name='dismissal_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата переведення'),
        ),
        migrations.AlterField(
            model_name='transferinstate',
            name='order_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='№ наказу'),
        ),
        migrations.AlterField(
            model_name='vocation',
            name='comment',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Примітки'),
        ),
        migrations.AlterField(
            model_name='vocation',
            name='order_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='№ наказу'),
        ),
        migrations.AlterField(
            model_name='vocation',
            name='period',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Період для відпустки'),
        ),
    ]
