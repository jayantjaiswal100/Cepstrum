# Generated by Django 3.1.2 on 2020-12-13 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='picture',
            field=models.URLField(default=None),
        ),
    ]
