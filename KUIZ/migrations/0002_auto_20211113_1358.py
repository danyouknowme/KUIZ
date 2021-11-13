# Generated by Django 3.2.7 on 2021-11-13 06:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('KUIZ', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 14, 6, 58, 28, 117442, tzinfo=utc), verbose_name='date end'),
        ),
        migrations.AlterField(
            model_name='type',
            name='correct',
            field=models.CharField(max_length=200),
        ),
    ]
