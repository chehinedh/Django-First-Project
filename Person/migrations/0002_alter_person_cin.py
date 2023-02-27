# Generated by Django 3.2.16 on 2023-02-06 11:07

import Person.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='cin',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[Person.models.cin_length], verbose_name='CIN'),
        ),
    ]