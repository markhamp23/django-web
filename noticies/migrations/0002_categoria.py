# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('titol_categoria', models.CharField(max_length=40, verbose_name='Titol de la categoria')),
            ],
            options={
                'ordering': ['titol_categoria'],
            },
        ),
    ]
