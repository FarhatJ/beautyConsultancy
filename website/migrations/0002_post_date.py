# Generated by Django 3.0.7 on 2020-06-29 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date(2020, 6, 29)),
        ),
    ]
