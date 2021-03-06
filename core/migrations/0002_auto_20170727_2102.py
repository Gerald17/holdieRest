# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 03:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenTarjeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='logos')),
            ],
            options={
                'verbose_name_plural': 'Logos',
            },
        ),
        migrations.CreateModel(
            name='Invitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailrecibe', models.EmailField(default='', max_length=254)),
                ('estado', models.IntegerField(choices=[(0, 'Pendiente'), (1, 'Aceptado'), (2, 'Rechazado')], default=0)),
            ],
            options={
                'verbose_name_plural': 'Invitaciones',
            },
        ),
        migrations.CreateModel(
            name='PerfilFavorito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Favoritos',
            },
        ),
        migrations.RemoveField(
            model_name='tarjeta',
            name='telefonos',
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='celular',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='logos'),
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='rubro',
            field=models.ForeignKey(default=28, on_delete=django.db.models.deletion.CASCADE, to='core.Rubro'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='telefono',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='favoritos',
            field=models.ManyToManyField(default=0, related_name='_perfil_favoritos_+', to='core.Tarjeta'),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='apellidos',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='direccion',
            field=models.TextField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='empresa',
            field=models.CharField(blank=True, default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='logo',
            field=models.ImageField(blank=True, upload_to='logos'),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='nombres',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='profesion',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='tags',
            field=models.ManyToManyField(blank=True, default=0, related_name='tarjetas', to='core.Tag'),
        ),
        migrations.AddField(
            model_name='perfilfavorito',
            name='tarjeta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tarjeta'),
        ),
        migrations.AddField(
            model_name='perfilfavorito',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invitacion',
            name='envia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitaciones_enviadas', to='core.Perfil'),
        ),
        migrations.AddField(
            model_name='invitacion',
            name='recibe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitaciones_recibidas', to='core.Perfil'),
        ),
        migrations.AddField(
            model_name='invitacion',
            name='tarjeta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tarjeta'),
        ),
    ]
