from django.contrib import admin
# !/usr/bin/env python
# -*- coding: utf-8 -*-
from core.models import *


# Se le debe crear a la tarjeta una fecha de creacion.

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


class RubroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')


class ProfesionAdmin(admin.ModelAdmin):
    list_display = ('id', 'rubro', 'nombre', 'descripcion')


class PaisAdmin(admin.ModelAdmin):
    list_display = ('cca2', 'nombre', 'telefono')


class PlantillaTarjetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


class TarjetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'plantilla', 'profesion', 'logo')


class PerfilFavoritoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'tarjeta')

class InvitacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado', 'envia', 'recibe', 'tarjeta', 'emailrecibe')


class ImagenTarjetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'imagen')

admin.site.register(Tag, TagAdmin)
admin.site.register(Rubro, RubroAdmin)
admin.site.register(Profesion, ProfesionAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(TelefonoUsuario)
admin.site.register(PlantillaTarjeta, PlantillaTarjetaAdmin)
admin.site.register(Tarjeta, TarjetaAdmin)
admin.site.register(Perfil)
admin.site.register(PerfilFavorito, PerfilFavoritoAdmin)
admin.site.register(Invitacion, InvitacionAdmin)
admin.site.register(ImagenTarjeta, ImagenTarjetaAdmin)
