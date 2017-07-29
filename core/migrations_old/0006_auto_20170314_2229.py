# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 04:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170314_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rubro',
            name='profesion',
        ),
        migrations.RemoveField(
            model_name='tarjeta',
            name='rubro',
        ),
        migrations.AddField(
            model_name='profesion',
            name='rubro',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Rubro'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='profesion',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Profesion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profesion',
            name='nombre',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='rubro',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
