# Generated by Django 3.2.6 on 2021-11-07 05:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('KUIZ', '0004_alter_quiz_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 8, 5, 55, 3, 499690, tzinfo=utc), verbose_name='date end'),
        ),
    ]