#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from core.models import *
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id',
                  'password',
                  'first_name',
                  'last_name',
                  'email', )
        write_only_fields = ('password',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProfesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesion
        fields = '__all__'


class RubroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubro
        fields = '__all__'


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'


class TelefonoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefonoUsuario
        fields = '__all__'


class TelefonoUsuarioSerializerWithoutUser(serializers.ModelSerializer):
    class Meta:
        model = TelefonoUsuario
        fields = ('pais', 'telefono')


class PlantillaTarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantillaTarjeta
        fields = '__all__'


class TarjetaSerializer(serializers.ModelSerializer):
    # telefonos = TelefonoUsuarioSerializerWithoutUser(many=True, readonly_fields)

    class Meta:
        model = Tarjeta
        fields = '__all__'
        read_only_fields = ('id', 'logo', 'fecha_creacion' )


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class PerfilFavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilFavorito
        fields = '__all__'

#Cambio Gerald
class ImagenTarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenTarjeta
        fields = '__all__'


class InvitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitacion
        fields = '__all__'



class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        pass

