# Generated by Django 3.1.3 on 2021-02-18 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pieces', '0014_auto_20210218_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpiece',
            name='uploader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='friendship_creator_set', to='auth.user'),
            preserve_default=False,
        ),
    ]
