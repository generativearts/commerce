# Generated by Django 2.2.12 on 2021-11-05 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20211105_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 5, 12, 48, 29, 262156), null=True),
        ),
    ]
