#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.template.defaultfilters import slugify as default_slugify


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=30)
    slug = models.SlugField(unique=True, max_length=100)

    @classmethod
    def slugify(cls, tag):
        return default_slugify(tag)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = Tag.slugify(self.name)
        return super(Tag, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Tags'


class Rubro(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    class Meta:
        verbose_name_plural = 'Rubros'
        db_table = "core_rubros"

    def __str__(self):
        return self.nombre


class Profesion(models.Model): #rubro
    rubro = models.ForeignKey('Rubro')
    nombre = models.CharField(max_length=15)
    descripcion = models.TextField()

    class Meta:
        verbose_name_plural = 'Profesiones'
        db_table = "core_profesions"

    def __str__(self):
        return self.nombre


class Pais(models.Model):
    cca2 = models.CharField(max_length=2, primary_key=True)
    telefono = models.CharField(max_length=3)
    nombre = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.nombre


class TelefonoUsuario(models.Model):
    usuario = models.ForeignKey(User)
    pais = models.ForeignKey('Pais')
    telefono = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = 'Telefonos Usuarios'

    def __str__(self):
        return self.telefono


class PlantillaTarjeta(models.Model):
    nombre = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = 'Plantillas de tarjetas'

    def __str__(self):
        return self.nombre


def upload_path(instance, filename):
    return '%s/logos/%d-%s' % (instance.usuario.id, instance.id, filename)


class Tarjeta(models.Model):
    usuario = models.ForeignKey(User)
    plantilla = models.ForeignKey('PlantillaTarjeta')
    #telefonos = models.ManyToManyField('TelefonoUsuario', related_name='+')
    telefono = models.CharField(max_length=30, blank=True)
    celular = models.CharField(max_length=30, blank=True)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    pais = models.ForeignKey('Pais')
    rubro = models.ForeignKey('Rubro')
    profesion = models.CharField(max_length=70)
    email = models.EmailField()
    empresa = models.CharField(max_length=50, blank=True, default=0)
    direccion = models.TextField(blank=True, default=0)
    imagen = models.ImageField(upload_to='logos', blank=True)
    #logo = models.TextField(db_column='data', blank=True, default='')
    logo = models.ImageField(upload_to='logos', blank=True)
    tags = models.ManyToManyField('Tag', related_name='tarjetas', blank=True, default=0)
    fecha_creacion = models.DateField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name_plural = 'Tarjetas'


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario

    class Meta:
        verbose_name_plural = 'Perfiles'

#Cambio Gerald

class ImagenTarjeta(models.Model):
    imagen = models.ImageField(upload_to='logos')

    class Meta:
        verbose_name_plural = 'Logos'

    def __str__(self):
        return self.imagen

class Invitacion(models.Model):
    estados = ((0, 'Pendiente'),(1, 'Aceptado'),(2, 'Rechazado'),)
    envia = models.ForeignKey(Perfil, related_name='invitaciones_enviadas')
    recibe = models.ForeignKey(Perfil, related_name='invitaciones_recibidas')
    emailrecibe = models.EmailField(default='')
    tarjeta = models.ForeignKey(Tarjeta)
    estado = models.IntegerField(default=0, choices=estados)

    class Meta:
        verbose_name_plural = 'Invitaciones'


class PerfilFavorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tarjeta = models.ForeignKey(Tarjeta)
   #favoritos = models.ManyToManyField('Tarjeta', related_name='+')

    class Meta:
        verbose_name_plural = 'Favoritos'


class Evento(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    empresa = models.CharField(max_length=30, blank=True)
    correo = models.CharField(max_length=50, blank=True)
    descripcion = models.TextField(max_length=300)
    fecha_creacion = models.DateField(auto_now_add=True, blank=True)

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
        #Perfil.objects.create(usuario=instance)


#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.perfil.save()


@receiver(pre_save, sender=User)
def set_username(sender, instance, **kwargs):
    instance.username = instance.email


@receiver(pre_save, sender=Tarjeta)
def set_filename(sender, instance, **kwargs):
    instance.username = instance.email