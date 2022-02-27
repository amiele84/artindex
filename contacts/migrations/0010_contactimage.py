# Generated by Django 3.1.7 on 2022-01-09 07:00

import contacts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_auto_20210321_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=contacts.models.upload_contact_image)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='contacts.contact')),
            ],
        ),
    ]
