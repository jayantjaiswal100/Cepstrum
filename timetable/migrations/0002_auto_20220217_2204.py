# Generated by Django 3.1.2 on 2022-02-17 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetable',
            old_name='year',
            new_name='roll_number',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='branch',
        ),
    ]
