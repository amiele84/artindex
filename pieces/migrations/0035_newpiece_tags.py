# Generated by Django 3.1.3 on 2021-03-04 03:17

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('pieces', '0034_remove_newpiece_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpiece',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
