# Generated by Django 2.2.12 on 2021-11-09 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0043_auto_20211109_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_bids_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 9, 13, 29, 57, 67404), null=True),
        ),
    ]
