# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-03 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('dept', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('moto', models.TextField()),
            ],
            options={
                'db_table': 'team',
            },
        ),
    ]
