# Generated by Django 3.1.7 on 2021-03-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20210321_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='job_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
