# Generated by Django 3.1.7 on 2021-12-27 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0068_newpiece_edition_dom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpiece',
            name='dim',
            field=models.CharField(choices=[('inches', 'INCHES'), ('centimeters', 'CENTIMETERS')], default='inches', max_length=15),
        ),
    ]
