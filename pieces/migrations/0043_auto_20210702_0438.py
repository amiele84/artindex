# Generated by Django 3.1.7 on 2021-07-02 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0042_auto_20210320_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpiece',
            name='title',
            field=models.CharField(help_text='Add Title', max_length=200),
        ),
    ]
