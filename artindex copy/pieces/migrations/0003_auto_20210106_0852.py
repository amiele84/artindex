# Generated by Django 3.1.3 on 2021-01-06 08:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0002_auto_20210106_0847'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='piece',
            options={'ordering': ['artist', 'upload_name']},
        ),
        migrations.AddField(
            model_name='piece',
            name='upload_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
