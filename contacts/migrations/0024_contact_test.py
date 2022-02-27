# Generated by Django 3.1.7 on 2022-01-20 04:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0023_auto_20220120_0441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_test',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='unique uuid for contact', primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='First Name', max_length=200)),
                ('middle_name', models.CharField(default='Middle Name', max_length=200)),
                ('last_name', models.CharField(default='Last Name', max_length=200)),
                ('job_title', models.CharField(blank=True, default='Job Title', max_length=200, null=True)),
                ('company', models.CharField(blank=True, default='Company', max_length=200, null=True)),
                ('email', models.CharField(blank=True, default='Email', max_length=200, null=True)),
                ('phone_number', models.CharField(blank=True, default='Phone Number', max_length=200, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('death_date', models.DateField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, default='Bio', max_length=1000, null=True)),
                ('notes', models.TextField(blank=True, default='Notes', max_length=1000, null=True)),
                ('birth_year', models.CharField(default='YY', max_length=4)),
                ('birth_month', models.CharField(default='MM', max_length=2)),
                ('birth_day', models.CharField(default='DD', max_length=2)),
                ('death_year', models.CharField(default='YY', max_length=4)),
                ('death_month', models.CharField(default='MM', max_length=2)),
                ('death_day', models.CharField(default='DD', max_length=2)),
                ('city', models.CharField(default='city', max_length=50)),
                ('state', models.CharField(blank=True, default='state', max_length=5, null=True)),
                ('zip_code', models.CharField(blank=True, default='zip', max_length=10, null=True)),
                ('contact_types', models.CharField(choices=[('Work', 'WORK'), ('Home', 'HOME'), ('Other', 'OTHER')], default='WORK', max_length=5)),
                ('contact_image', models.ImageField(upload_to='images/')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]
