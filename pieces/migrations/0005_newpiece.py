# Generated by Django 3.1.3 on 2021-01-06 10:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0004_auto_20210106_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewPiece',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this piece instance', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='Add Description', max_length=500)),
                ('medium', models.CharField(max_length=200)),
                ('subject_matter', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('depth', models.IntegerField()),
                ('price', models.IntegerField()),
                ('piece_upload', models.ImageField(upload_to='images/')),
                ('date_of_upload', models.DateField(blank=True, null=True)),
                ('types', models.CharField(blank=True, choices=[('painting', 'PAINTING'), ('sculpture', 'SCULPTURE'), ('textile', 'TEXTTILE'), ('photograph', 'PHOTOGRAPH'), ('none', 'NONE')], default='none', help_text='type', max_length=10)),
                ('dim', models.CharField(blank=True, choices=[('inches', 'INCHES'), ('centimeters', 'CENTIMETERS')], default='none', help_text='type', max_length=15)),
                ('visibility', models.CharField(blank=True, choices=[('Private', 'PRIVATE'), ('Public', 'PUBLIC')], default='none', help_text='type', max_length=10)),
                ('availability', models.CharField(blank=True, choices=[('Unfinished', 'UNFINISHED'), ('Complete', 'COMPLETE'), ('Pending', 'PENDING'), ('Sold', 'SOLD')], default='none', help_text='type', max_length=10)),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pieces.artist')),
            ],
            options={
                'ordering': ['artist', 'title'],
            },
        ),
    ]
