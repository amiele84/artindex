# Generated by Django 3.1.7 on 2021-03-20 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0041_auto_20210320_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpiece',
            name='visibility',
            field=models.CharField(blank=True, choices=[('Private', 'PRIVATE'), ('Public', 'PUBLIC')], help_text='type', max_length=10),
        ),
    ]
