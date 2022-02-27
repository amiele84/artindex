# Generated by Django 3.1.7 on 2022-01-14 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0016_auto_20220113_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='birth_day',
            field=models.CharField(default='D', max_length=2),
        ),
        migrations.AlterField(
            model_name='contact',
            name='birth_month',
            field=models.CharField(default='M', max_length=2),
        ),
        migrations.AlterField(
            model_name='contact',
            name='death_day',
            field=models.CharField(default='D', max_length=2),
        ),
        migrations.AlterField(
            model_name='contact',
            name='death_month',
            field=models.CharField(default='M', max_length=2),
        ),
    ]
