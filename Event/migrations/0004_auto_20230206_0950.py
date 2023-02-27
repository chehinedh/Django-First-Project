# Generated by Django 3.2.16 on 2023-02-06 08:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0003_auto_20230206_0948'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='event',
            name='date doit etre > a date systeme',
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.CheckConstraint(check=models.Q(('event_date__gte', datetime.datetime(2023, 2, 6, 9, 50, 27, 876239))), name='date doit etre > a date systeme'),
        ),
    ]