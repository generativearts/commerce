# Generated by Django 3.2.8 on 2021-11-03 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20211103_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 3, 23, 18, 17, 322538), null=True),
        ),
    ]
