# Generated by Django 2.0.5 on 2018-12-05 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('certificate', '0012_auto_20181204_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostQualificationLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thickness', models.CharField(max_length=300, verbose_name='Товщина')),
                ('bulgarian', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certificate.Bulgarian', verbose_name='Вміння працювати болгаркою')),
                ('candle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certificate.Candle', verbose_name='Вміння працювати з газовим паяльником')),
                ('connection_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certificate.ConnectionType', verbose_name="Тип з'єднання")),
                ('draw_reading', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certificate.DrawReading', verbose_name='Читання креслень')),
                ('metal_brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certificate.MetalBrand', verbose_name='Марка металу')),
            ],
            options={
                'verbose_name': 'Попередня оцінка кваліфікації',
                'verbose_name_plural': 'Попередня оцінки кваліфікації',
            },
        ),
        migrations.RemoveField(
            model_name='prequalificationlevel',
            name='bulgarian',
        ),
        migrations.RemoveField(
            model_name='prequalificationlevel',
            name='candle',
        ),
        migrations.RemoveField(
            model_name='prequalificationlevel',
            name='connection_type',
        ),
        migrations.RemoveField(
            model_name='prequalificationlevel',
            name='draw_reading',
        ),
        migrations.RemoveField(
            model_name='prequalificationlevel',
            name='metal_brand',
        ),
        migrations.RemoveField(
            model_name='prequalificationlevel',
            name='other',
        ),
        migrations.RemoveField(
            model_name='prequalificationlevel',
            name='semiautomatic',
        ),
        migrations.RemoveField(
            model_name='prequalificationlevel',
            name='spatial_posture',
        ),
        migrations.RemoveField(
            model_name='prequalificationlevel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='prequalificationlevel',
            name='welding_method',
        ),
        migrations.AlterModelOptions(
            name='other',
            options={'verbose_name': 'Рівень кваліфікації', 'verbose_name_plural': 'Рівні кваліфікації'},
        ),
        migrations.AlterField(
            model_name='other',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Рівень кваліфікації'),
        ),
        migrations.AlterField(
            model_name='qualificationlevel',
            name='other',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certificate.Other', verbose_name='Рівень кваліфікації'),
        ),
        migrations.DeleteModel(
            name='PreQualificationLevel',
        ),
        migrations.AddField(
            model_name='postqualificationlevel',
            name='other',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certificate.Other', verbose_name='Оцінка кваліфікації'),
        ),
        migrations.AddField(
            model_name='postqualificationlevel',
            name='semiautomatic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certificate.SemiAutomatic', verbose_name='Досвід зварювання напівавтоматом'),
        ),
        migrations.AddField(
            model_name='postqualificationlevel',
            name='spatial_posture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certificate.SpatialPosture', verbose_name='Просторове положення'),
        ),
        migrations.AddField(
            model_name='postqualificationlevel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='post_qualifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postqualificationlevel',
            name='welding_method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certificate.WeldMethod', verbose_name='Спосіб зварювання'),
        ),
    ]
