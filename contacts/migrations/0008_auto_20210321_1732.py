# Generated by Django 3.1.7 on 2021-03-21 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_auto_20210321_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_types',
            field=models.CharField(blank=True, choices=[('Work', 'WORK'), ('Home', 'HOME'), ('Other', 'OTHER')], default='none', help_text='type', max_length=5),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
