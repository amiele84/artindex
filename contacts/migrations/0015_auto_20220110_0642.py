# Generated by Django 3.1.7 on 2022-01-10 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0014_auto_20220110_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='bio',
            field=models.TextField(blank=True, default='Bio', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='notes',
            field=models.TextField(blank=True, default='Notes', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(blank=True, default='Phone Number', max_length=200, null=True),
        ),
    ]
