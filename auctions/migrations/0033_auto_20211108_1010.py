# Generated by Django 2.2.12 on 2021-11-08 10:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0032_auto_20211108_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 8, 10, 9, 59, 714724), null=True),
        ),
    ]