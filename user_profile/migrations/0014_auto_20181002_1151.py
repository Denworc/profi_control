# Generated by Django 2.0.5 on 2018-10-02 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0013_remove_user_personal_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['sort'], 'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакти'},
        ),
        migrations.AlterModelOptions(
            name='contacttype',
            options={'verbose_name': 'Тип контакта', 'verbose_name_plural': 'Типи контактів'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Користувач', 'verbose_name_plural': 'Користувачі'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='sort',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Порядок сортування'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата народження'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=40, verbose_name='Прізвище'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Суперюзер'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_worker',
            field=models.BooleanField(default=True, verbose_name='Клієнт'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=40, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(blank=True, max_length=30, unique=True, verbose_name='Логін'),
        ),
        migrations.AlterField(
            model_name='user',
            name='patronymic',
            field=models.CharField(max_length=40, verbose_name='По-батькові'),
        ),
    ]
