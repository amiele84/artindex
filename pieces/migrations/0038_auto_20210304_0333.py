# Generated by Django 3.1.3 on 2021-03-04 03:33

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('pieces', '0037_auto_20210304_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpiece',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='pieces.UUIDTaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='uuidtaggeditem',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pieces_uuidtaggeditem_items', to='taggit.tag'),
        ),
    ]
