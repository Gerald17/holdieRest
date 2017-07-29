#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import viewsets, status
from api.serializers import *
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import list_route, detail_route, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from django.shortcuts import get_object_or_404
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from django.db.models import Q
import unicodedata
from django.db.models import ImageField

class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,
                         'id': user.id,
                         'first_name': user.first_name,
                         'last_name': user.last_name,
                         'email': user.email})


obtain_auth_token = ObtainAuthToken.as_view()


class OwnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated():
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or (obj.usuario == request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            u = User.objects.filter(email=serialized.data['email'])
            if len(u) > 0:
                return Response({"email": ["Account with supplied email already exists."]},
                                status=status.HTTP_409_CONFLICT)
            User.objects.create_user(
                email=serialized.data['email'],
                username=serialized.data['email'],
                password=serialized.data['password'],
                first_name=serialized.data['first_name'],
                last_name=serialized.data['last_name'],
            )
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['post'])
    def update_password(self, request, *args, **kwargs):
        user = self.request.user
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not user.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            user.set_password(serializer.data.get("new_password"))
            user.save()
            user.password = ""
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ProfesionViewSet(viewsets.ModelViewSet):
    queryset = Profesion.objects.all()
    serializer_class = ProfesionSerializer


class RubroViewSet(viewsets.ModelViewSet):
    queryset = Rubro.objects.all()
    serializer_class = RubroSerializer


class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer


class TelefonoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TelefonoUsuario.objects.all()
    serializer_class = TelefonoUsuarioSerializer
    permission_classes = (OwnerPermission,)

    def get_queryset(self):
        return TelefonoUsuario.objects.filter(usuario=self.request.user)


class PlantillaTarjetaViewSet(viewsets.ModelViewSet):
    queryset = PlantillaTarjeta.objects.all()
    serializer_class = PlantillaTarjetaSerializer


class TarjetaViewSet(viewsets.ModelViewSet):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer

    #def get_queryset(self):
    #    return Tarjeta.objects.filter(usuario=self.request.user)



class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    permission_classes = (OwnerPermission,)


class PerfilFavoritoViewSet(viewsets.ModelViewSet):
    queryset = PerfilFavorito.objects.all()
    serializer_class = PerfilFavoritoSerializer
    permission_classes = (OwnerPermission,)

    def get_queryset(self):
        return PerfilFavorito.objects.filter(usuario=self.request.user)


# Cambio Gerald
class ImagenTarjetaViewSet(viewsets.ModelViewSet):
    queryset = ImagenTarjeta.objects.all()
    serializer_class = ImagenTarjetaSerializer

class InvitacionViewSet(viewsets.ModelViewSet):
    queryset = Invitacion.objects.all()
    serializer_class = InvitacionSerializer
    permission_classes = (OwnerPermission,)

    # def get_queryset(self):
    # perfil=get_object_or_404(Perfil, usuario=self.request.user)
    # return Invitacion.objects.filter(Q(recibe=perfil) | Q(envia=perfil))

