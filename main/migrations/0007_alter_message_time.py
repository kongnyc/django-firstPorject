# Generated by Django 3.2.7 on 2021-10-22 21:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20211022_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 21, 9, 9, 805237, tzinfo=utc)),
        ),
    ]
