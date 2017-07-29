#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api.views import *
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'profesiones', ProfesionViewSet)
router.register(r'rubros', RubroViewSet)
router.register(r'paises', PaisViewSet)
router.register(r'telefonos', TelefonoUsuarioViewSet)
router.register(r'plantillas', PlantillaTarjetaViewSet)
router.register(r'tarjetas', TarjetaViewSet)
router.register(r'perfil', PerfilViewSet)
router.register(r'usuarios', UserViewSet)
router.register(r'invitacion', InvitacionViewSet)
router.register(r'favorito', PerfilFavoritoViewSet)
router.register(r'imagenes', ImagenTarjetaViewSet)
# router.register(r'password', ChangePasswordView)


urlpatterns = [
    url(r'^login/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)