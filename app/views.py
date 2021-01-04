# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from app import models



@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def actuusuario(request):
    context = {}
    try:
        if request.method=='POST':
            iduser= request.POST['iduser']
            nombre = request.POST['nombre'] 
            numero = request.POST['numero']
            correo  = request.POST['correo']
            company = request.POST['company']
            rol = request.POST['rol']
            estado = request.POST['status']
            usuario=models.User.objects.get(userid=iduser)
            usuario.accountname = nombre
            usuario.accountcellphone = numero
            usuario.accountemail = correo
            if (company!=''):
                usuario.company_companyid = models.Company.objects.get(name=company)
            if (rol!=''):
                usuario.rol_rolid = models.Rol.objects.get(name=rol)
            if (estado!=''):
                usuario.status_statusid =models.Statususer.objects.get(name=estado)
            usuario.save()
        usuarios=models.User.objects.all()
        return render(request,"Clientes.html",{'clientes':usuarios})
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def usuarios(request):
    context = {}
    try:
        usuarios=models.User.objects.all()
        return render(request,"Clientes.html",{'clientes':usuarios})
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def companys(request):
    context = {}
    try:
        companys=models.Company.objects.all()
        return render(request,"company.html",{'companys':companys})
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def productos(request):
    context = {}
    company = {}
    try:
        if request.method=='POST':
            idcom= request.POST['idcom']
            productos=models.Product.objects.filter(company_companyid=idcom)
            company=models.Company.objects.get(companyid=idcom)
        else:
            productos = models.Product.objects.all()
        return render(request,"productos.html",{'productos':productos,'company':company})
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def planes(request):
    context = {}
    try:
        planes=models.Plan.objects.all()
        return render(request,"planes.html",{'planes':planes})
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def datosusuario(request):
    context = {}
    try:
        if request.method=='POST':
            iduser= request.POST['iduser']
            usuario=models.User.objects.get(userid=iduser)
            statususer=models.Statususer.objects.all()
            company=models.Company.objects.all()
            rol=models.Rol.objects.all()
            return render(request,"datosusuario.html",{'usuario':usuario,'estados':statususer,'companys':company,'roles':rol})
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def datoscompany(request):
    context = {}

    if request.method=='POST':
        idcom= request.POST['idcom']
        company=models.Company.objects.get(companyid=idcom)
        statuscompany=models.Statuscompany.objects.all()
        companytype=models.Companytype.objects.all()
        appformulary=models.Appformulary.objects.all()
        return render(request,"datoscompany.html",{'company':company,'estados':statuscompany,'tipos':companytype,'formularios':appformulary})

@login_required(login_url="/login/")
def datosproducto(request):
    context = {}
    try:
        if request.method=='POST':
            idpro= request.POST['idpro']
            producto=models.Product.objects.get(productid=idpro)
            productstatus=models.Productstatus.objects.all()
            company=models.Company.objects.all()
            typeproduct=models.Typeproduct.objects.all()
            return render(request,"datosproducto.html",{'producto':producto,'estados':productstatus,'companys':company,'tipos':typeproduct})
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
    


@login_required(login_url="/login/")
def actuproducto(request):
    context = {}
    company = {}
    try:
        if request.method=='POST':
            idpro= request.POST['idpro']
            nombre = request.POST['nombre'] 
            costo = request.POST['costo']
            descripcion  = request.POST['descripcion']
            descuento  = request.POST['descuento']
            company = request.POST['empresa']
            tipo = request.POST['tipo']
            estado = request.POST['estado']
            producto=models.Product.objects.get(productid=idpro)
            producto.nameproduct = nombre
            producto.costproduct = costo
            producto.description = descripcion
            producto.disccount = descuento
            if (company!=''):
                producto.company_companyid = models.Company.objects.get(name=company)
            if (tipo!=''):
                producto.rol_rolid = models.Typeproduct.objects.get(name=tipo)
            if (estado!=''):
                producto.productstatusid =models.Productstatus.objects.get(productstatusdescription=estado)
            producto.save()
        productos = models.Product.objects.all()
        return render(request,"productos.html",{'productos':productos,'company':company})
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def actucompany(request):
    context = {}
    company = {}
    try:
        if request.method=='POST':
            idpro= request.POST['idpro']
            nombre = request.POST['nombre'] 
            costo = request.POST['costo']
            descripcion  = request.POST['descripcion']
            descuento  = request.POST['descuento']
            company = request.POST['empresa']
            tipo = request.POST['tipo']
            estado = request.POST['estado']
            producto=models.Product.objects.get(productid=idpro)
            producto.nameproduct = nombre
            producto.costproduct = costo
            producto.description = descripcion
            producto.disccount = descuento
            if (company!=''):
                producto.company_companyid = models.Company.objects.get(name=company)
            if (tipo!=''):
                producto.rol_rolid = models.Typeproduct.objects.get(name=tipo)
            if (estado!=''):
                producto.productstatusid =models.Productstatus.objects.get(productstatusdescription=estado)
            producto.save()
        productos = models.Product.objects.all()
        return render(request,"productos.html",{'productos':productos,'company':company})
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))