# Generated by Django 3.1.3 on 2021-02-19 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0022_auto_20210219_0546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newpiece',
            old_name='user',
            new_name='uploader',
        ),
    ]
