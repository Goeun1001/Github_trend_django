# Generated by Django 3.2.3 on 2021-06-04 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Repository', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]