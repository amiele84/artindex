# Generated by Django 3.1.7 on 2021-03-20 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0038_auto_20210304_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpiece',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pieces.artist'),
        ),
    ]
