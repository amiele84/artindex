# Generated by Django 3.1.7 on 2021-12-27 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0063_newpiece2_pieceimage2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpiece',
            name='types',
            field=models.CharField(choices=[('painting', 'PAINTING'), ('sculpture', 'SCULPTURE'), ('textile', 'TEXTTILE'), ('photograph', 'PHOTOGRAPH'), ('none', 'NONE')], default='painting', max_length=10),
        ),
    ]
