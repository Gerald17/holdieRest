# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 04:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170314_2229'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='profesion',
            table='core_profesions',
        ),
        migrations.AlterModelTable(
            name='rubro',
            table='core_rubros',
        ),
    ]
