# Generated by Django 3.1.2 on 2021-05-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='linkeden',
            field=models.URLField(blank=True, null=True),
        ),
    ]
