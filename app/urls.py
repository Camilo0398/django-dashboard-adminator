# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.dashboard, name='home'),
    path('actuusuario', views.actuusuario, name='actuusuario'),
    path('actuproducto', views.actuproducto, name='actuproducto'),
    path('actucompany', views.actucompany, name='actucompany'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('companys', views.companys, name='companys'),
    path('productos', views.productos, name='productos'),
    path('planes', views.planes, name='planes'),
    path('el', views.eliminar, name='eliminar'),
    path('crearproducto', views.crearproducto, name='crearproducto'),
    path('crearcompany', views.crearcompany, name='crearcompany'),
    path('add', views.adicionar, name='adicionar'),
    path('adduser', views.adduser, name='adduser'),
    path('addproduct', views.addproduct, name='addproduct'),
    path('addcompany', views.addcompany, name='addcompany'),
    path('emails', views.emails, name='emails'),
    path('usuarios.datosusuario', views.datosusuario, name='datosusuario'),
    path('companys.datoscompany', views.datoscompany, name='datoscompany'),
    path('companys.datosproducto', views.datosproducto, name='datosproducto'),
    path('tablacc<companyid>', views.tabla, name='tabla'),

]
