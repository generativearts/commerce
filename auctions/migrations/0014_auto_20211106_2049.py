# Generated by Django 3.2.8 on 2021-11-06 18:49

import auctions.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20211106_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 6, 20, 49, 17, 670628), null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=auctions.models.path_and_rename),
        ),
    ]