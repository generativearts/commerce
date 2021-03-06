# Generated by Django 3.2.8 on 2021-11-08 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0038_auto_20211108_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 8, 21, 32, 47, 18141), null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_start_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
    ]
