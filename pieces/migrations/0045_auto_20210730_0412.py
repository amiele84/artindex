# Generated by Django 3.1.7 on 2021-07-30 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0044_auto_20210730_0304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piconly',
            old_name='upload_pic',
            new_name='upload',
        ),
    ]
