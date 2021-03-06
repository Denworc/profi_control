# Generated by Django 2.0.5 on 2018-11-15 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0014_auto_20181114_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Підприємство-роботодавець')),
            ],
            options={
                'verbose_name': 'Підприємство-роботодавець',
                'verbose_name_plural': 'Підприємства-роботодавці',
            },
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Завод')),
            ],
            options={
                'verbose_name': 'Завод',
                'verbose_name_plural': 'Заводи',
            },
        ),
        migrations.CreateModel(
            name='Voivodship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Воєводство')),
            ],
            options={
                'verbose_name': 'Воєводство',
                'verbose_name_plural': 'Воєводства',
            },
        ),
        migrations.AlterField(
            model_name='permission',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to='work.Employer', verbose_name='Підприємство-роботодавець'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='factory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to='work.Factory', verbose_name='Завод'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='voivodship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to='work.Voivodship', verbose_name='Воєводство'),
        ),
    ]
