# Generated by Django 2.1 on 2019-12-24 01:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imei', models.CharField(max_length=128, unique=True)),
                ('full_name', models.CharField(max_length=128)),
                ('model', models.CharField(max_length=128)),
                ('storage', models.CharField(max_length=128)),
                ('color', models.CharField(max_length=128)),
                ('grade', models.CharField(max_length=128)),
                ('product_id', models.CharField(max_length=128)),
                ('date_in', models.DateTimeField(default=datetime.datetime(2019, 12, 24, 12, 4, 50, 566000))),
                ('date_out', models.DateTimeField()),
                ('date_modified', models.DateTimeField(default=datetime.datetime(2019, 12, 24, 12, 4, 50, 566000))),
                ('change_checked', models.BooleanField(default=False)),
                ('input_confirmed', models.BooleanField(default=False)),
            ],
        ),
    ]
