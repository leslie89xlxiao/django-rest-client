# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 08:22
from __future__ import unicode_literals

from django.db import migrations, models
import jsoneditor.fields.django_jsonfield


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoRestClient',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('config', jsoneditor.fields.django_jsonfield.JSONField(default={})),
            ],
            options={
                'db_table': 'django_rest_client',
            },
        ),
    ]
