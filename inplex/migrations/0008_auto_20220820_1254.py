# Generated by Django 3.1.2 on 2022-08-20 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inplex', '0007_auto_20220820_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='difficulty2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='two', to='inplex.difficulty'),
        ),
    ]
