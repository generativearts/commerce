# Generated by Django 3.2.8 on 2021-11-04 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20211104_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 4, 18, 11, 26, 222544), null=True),
        ),
    ]