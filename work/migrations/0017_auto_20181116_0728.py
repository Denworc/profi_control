# Generated by Django 2.0.5 on 2018-11-16 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0016_auto_20181115_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptioninstate',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adoptions', to='work.Employer', verbose_name='Підприємство-роботодавець'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='factory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment', to='work.Factory', verbose_name='Завод'),
        ),
        migrations.AlterField(
            model_name='incomingcontrol',
            name='factory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming_controls', to='work.Factory', verbose_name='Завод'),
        ),
    ]
