# Generated by Django 3.1.7 on 2021-10-20 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0060_geeksmodel_upload_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geeksmodel',
            name='upload_pic',
            field=models.ImageField(blank=True, upload_to='pieces/images/'),
        ),
    ]
