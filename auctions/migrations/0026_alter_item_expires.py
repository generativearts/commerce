# Generated by Django 3.2.8 on 2021-11-08 05:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0025_auto_20211107_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 8, 7, 53, 25, 330660), null=True),
        ),
    ]
