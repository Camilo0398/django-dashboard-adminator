# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('actuusuario', views.actuusuario, name='actuusuario'),
    path('actuproducto', views.actuproducto, name='actuproducto'),
    path('actucompany', views.actucompany, name='actucompany'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('companys', views.companys, name='companys'),
    path('productos', views.productos, name='productos'),
    path('planes', views.planes, name='planes'),
    path('usuarios.datosusuario', views.datosusuario, name='datosusuario'),
    path('companys.datoscompany', views.datoscompany, name='datoscompany'),
    path('companys.datosproducto', views.datosproducto, name='datosproducto'),
    # # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
