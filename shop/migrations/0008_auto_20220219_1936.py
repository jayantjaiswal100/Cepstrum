# Generated by Django 3.1.2 on 2022-02-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_order_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.AddField(
            model_name='checkoutaddress',
            name='name',
            field=models.CharField(default='', max_length=15),
        ),
    ]
