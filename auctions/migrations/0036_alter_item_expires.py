# Generated by Django 3.2.8 on 2021-11-08 18:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0035_auto_20211108_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 8, 20, 51, 34, 934260), null=True),
        ),
    ]
