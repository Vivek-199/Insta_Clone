# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=0)),
                ('has_verified_mobile', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
