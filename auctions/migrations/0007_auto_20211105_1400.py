# Generated by Django 2.2.12 on 2021-11-05 14:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20211105_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 5, 14, 0, 12, 250168), null=True),
        ),
    ]
