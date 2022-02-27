# Generated by Django 3.1.7 on 2022-01-20 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0025_auto_20220120_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_test',
            name='city',
            field=models.CharField(default='city', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact_test',
            name='state',
            field=models.CharField(blank=True, default='state', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='contact_test',
            name='zip_code',
            field=models.CharField(blank=True, default='zip', max_length=10, null=True),
        ),
    ]
