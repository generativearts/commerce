# Generated by Django 3.2.8 on 2021-11-09 20:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0047_auto_20211109_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 9, 22, 18, 17, 880938), null=True),
        ),
    ]
