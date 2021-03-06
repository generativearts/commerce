# Generated by Django 3.2.8 on 2021-11-07 17:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import uuid

def gen_uuid(apps, schema_editor):
    MyModel = apps.get_model('auctions', 'Item')
    for row in MyModel.objects.all():
        row.uuid = uuid.uuid4()
        row.save()

class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20211107_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 7, 19, 53, 1, 919988), null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_code',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=36, null=True),
        ),
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='item',
            name='item_code',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=36, null=True),
        ),
    ]
