# Generated by Django 3.1.7 on 2022-01-14 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0018_auto_20220114_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_types',
            field=models.CharField(choices=[('Work', 'WORK'), ('Home', 'HOME'), ('Other', 'OTHER')], default='WORK', max_length=5),
        ),
    ]
