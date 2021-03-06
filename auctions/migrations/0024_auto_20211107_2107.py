# Generated by Django 3.2.8 on 2021-11-07 19:07

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_auto_20211107_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 7, 21, 7, 34, 263396), null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_UUID',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
    ]
