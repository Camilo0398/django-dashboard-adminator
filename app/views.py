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
from app.logica import bucket, mail, archivo, graficas

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
        return redirect(usuarios)
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
    

    if request.method=='POST':
        idcom= request.POST['idcom']
        company=models.Company.objects.get(companyid=idcom)
        statuscompany=models.Statuscompany.objects.all()
        companytype=models.Companytype.objects.all()
        appformulary=models.Appformulary.objects.all()
        company_city=models.CompanyCity.objects.all()
        city=models.City.objects.all()
        return render(request,"datoscompany.html",{'company':company,'estados':statuscompany,'tipos':companytype,'formularios':appformulary,'citycompany':company_city,'citys':city})

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
            
            if request.POST['descuento']:
                descuento  = request.POST['descuento']
            else:
                descuento = 0
            company = request.POST['empresa']
            tipo = request.POST['tipo']
            estado = request.POST['estado']
            producto=models.Product.objects.get(productid=idpro)
            producto.nameproduct = nombre
            producto.costproduct = costo
            producto.description = descripcion
            producto.disccount = descuento
            company2=models.Company.objects.get(name=company)
            name=company2.name
            if 'imgpro' in request.FILES:
                urlname = producto.imageurl
                bucket.borrarimg(name,urlname)
                imagen = request.FILES['imgpro']
                imgname = request.FILES['imgpro'].name
                urlcom= bucket.saveimage(imagen,name,imgname)
                producto.imageurl =urlcom
            if (company!=''):
                producto.company_companyid = models.Company.objects.get(name=company)
            if (tipo!=''):
                producto.typeproduct_typeproductid = models.Typeproduct.objects.get(name=tipo)
            if (estado!=''):
                producto.productstatusid =models.Productstatus.objects.get(productstatusdescription=estado)
            producto.save()
        return redirect(productos)
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
            idcom= request.POST['idcom']
       
            direccion = request.POST['direccion']
            contactnom  = request.POST['contactnom']
            contacttel  = request.POST['contacttel']
            correo = request.POST['correo']
            estado = request.POST['estado']
            tipo = request.POST['tipo']
            appform = request.POST['formuapp']
            company=models.Company.objects.get(companyid=idcom)
            name= company.name
            if 'rut' in request.FILES:
                urlname = company.ruturl
                bucket.borrarimg(name,urlname)
                rut = request.FILES['rut']
                namerut = request.FILES['rut'].name
                urlcom= bucket.savepdf(rut,name,namerut)
                company.ruturl =urlcom
            if 'imgcom' in request.FILES:
                urlname = company.imageurl
                bucket.borrarimg(name,urlname)
                imagencom = request.FILES['imgcom']
                nameimagencom = request.FILES['imgcom'].name
                urlcom= bucket.saveimage(imagencom,name,nameimagencom)
                company.imageurl =urlcom
            if 'imgappena' in request.FILES:
                urlname = company.imageappenabled
                bucket.borrarimg(name,urlname)
                imgappena = request.FILES['imgappena']
                nameimagappena = request.FILES['imgappena'].name
                urlcom= bucket.saveimage(imgappena,name,nameimagappena)
                company.imageappenabled =urlcom
            if 'imgappdisa' in request.FILES:
                urlname = company.imageappdisabled
                bucket.borrarimg(name,urlname)
                imgappdisa = request.FILES['imgappdisa']
                nameimagappdisa = request.FILES['imgappdisa'].name
                urlcom= bucket.saveimage(imgappdisa,name,nameimagappdisa)
                company.imageappdisabled =urlcom
            company.address = direccion
            company.contactname = contactnom
            company.contactphone = contacttel
            company.contactEmail = correo
            company.statuscompany_statuscompanyid = models.Statuscompany.objects.get(name=estado)
            company.companytype = models.Companytype.objects.get(companytypedescription=tipo)
            company.appformularyid =models.Appformulary.objects.get(appformularydescription=appform)
            company.save()
        return redirect(companys)
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def tabla(request, companyid):
    company=models.Company.objects.get(companyid=companyid)
    city=models.City.objects.all()
    CompanyCity=models.CompanyCity.objects.all()
    if "filtrarHooks" in request.POST:
        idcomc= request.POST['idcomc']
        companycity=models.CompanyCity.objects.get(companycityid=idcomc)
        companycity.delete()
    return render(request,"tablacc.html",{'citys':city,'companycity':CompanyCity,'company':company})
@login_required(login_url="/login/")
def eliminar(request):
    if request.method == 'GET':
        param1 = request.GET.get('param_first')
        companycity=models.CompanyCity.objects.get(companycityid=param1)
        companycity.delete()


        response_data = 'successful!'

        return HttpResponse()

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
@login_required(login_url="/login/")
def adicionar(request):
    if request.method == 'GET':
        company = request.GET.get('company')
        city = request.GET.get('city')
        valord = request.GET.get('valord')
        companycity=models.CompanyCity()
        companycity.company_companyid = company
        companycity.city_idcity =city
        companycity.deliveryvalue = valord
        companycity.save()

        return HttpResponse()

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@login_required(login_url="/login/")
def adduser(request):
    context = {}
    try:
        return render(request,'adduser.html')
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
        addproduct
@login_required(login_url="/login/")
def addproduct(request):
    context = {}
    try:
        
        productstatus=models.Productstatus.objects.all()
        company=models.Company.objects.all()
        typeproduct=models.Typeproduct.objects.all()
        return render(request,"addproduct.html",{'estados':productstatus,'companys':company,'tipos':typeproduct})
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def crearproducto(request):
    context = {}
    try:
        if request.method=='POST':
            idpro= request.POST['idpro']
            nombre = request.POST['nombre'] 
            costo = request.POST['costo']
            descripcion  = request.POST['descripcion']
            if request.POST['descuento']:
                descuento  = request.POST['descuento']
            else:
                descuento = 0
            company = request.POST['empresa']
            tipo = request.POST['tipo']
            estado = request.POST['estado']
            producto=models.Product()
            producto.nameproduct = nombre
            producto.costproduct = costo
            producto.description = descripcion
            producto.disccount = descuento
            company2=models.Company.objects.get(name=company)
            name=company2.name
            if 'imgpro' in request.FILES:
                urlname = producto.imageurl
                bucket.borrarimg(name,urlname)
                imagen = request.FILES['imgpro']
                imgname = request.FILES['imgpro'].name
                urlcom= bucket.saveimage(imagen,name,imgname)
                producto.imageurl =urlcom
            if (company!=''):
                producto.company_companyid = models.Company.objects.get(name=company)
            if (tipo!=''):
                producto.typeproduct_typeproductid = models.Typeproduct.objects.get(name=tipo)
            if (estado!=''):
                producto.productstatusid =models.Productstatus.objects.get(productstatusdescription=estado)
            producto.save()
        return redirect(productos)
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def addcompany(request):
    context = {}
    try:
        statuscompany=models.Statuscompany.objects.all()
        companytype=models.Companytype.objects.all()
        appformulary=models.Appformulary.objects.all()
        company_city=models.CompanyCity.objects.all()
        city=models.City.objects.all()
        return render(request,"addcompany.html",{'estados':statuscompany,'tipos':companytype,'formularios':appformulary,'citycompany':company_city,'citys':city})

    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def crearcompany(request):
    context = {}
    company = {}
    try:
        if request.method=='POST':
            name = request.POST['nombre']
            nit = request.POST['NIT']
            direccion = request.POST['direccion']
            contactnom  = request.POST['contactnom']
            contacttel  = request.POST['contacttel']
            correo = request.POST['correo']
            estado = request.POST['estado']
            tipo = request.POST['tipo']
            appform = request.POST['formuapp']
            company=models.Company()
            if 'rut' in request.FILES:
                rut = request.FILES['rut']
                namerut = request.FILES['rut'].name
                urlcom= bucket.savepdf(rut,name,namerut)
                company.ruturl =urlcom
            if 'imgcom' in request.FILES:
                imagencom = request.FILES['imgcom']
                nameimagencom = request.FILES['imgcom'].name
                urlcom= bucket.saveimage(imagencom,name,nameimagencom)
                company.imageurl =urlcom
            if 'imgappena' in request.FILES:
                imgappena = request.FILES['imgappena']
                nameimagappena = request.FILES['imgappena'].name
                urlcom= bucket.saveimage(imgappena,name,nameimagappena)
                company.imageappenabled =urlcom
            if 'imgappdisa' in request.FILES:
                imgappdisa = request.FILES['imgappdisa']
                nameimagappdisa = request.FILES['imgappdisa'].name
                urlcom= bucket.saveimage(imgappdisa,name,nameimagappdisa)
                company.imageappdisabled =urlcom
            company.name =name
            company.nit = nit
            company.address = direccion
            company.contactname = contactnom
            company.contactphone = contacttel
            company.contactEmail = correo
            company.statuscompany_statuscompanyid = models.Statuscompany.objects.get(name=estado)
            company.companytype = models.Companytype.objects.get(companytypedescription=tipo)
            company.appformularyid =models.Appformulary.objects.get(appformularydescription=appform)
            company.save()
        return redirect(companys)
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def emails(request):

    context = {}
    try:
        if request.method=='POST':
            asunto = request.POST['asunto']
            if request.POST['dest']:
                destinatarios = str(request.POST['dest'])
                destinatarios = destinatarios.split(",")
            else:
                destinatarios = models.User.objects.values_list('accountemail', flat=True)
                
            html = request.FILES['html']
            var = archivo.arreglarhtml(html)
            print(var)
            for destinatario in destinatarios:
                mail.enviarmail(destinatario,asunto,var)
        return render(request,"emails.html")
    
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def dashboard(request):
    context={}
    try:
        isonline = models.User.objects.values_list('isonline', flat=True)
        isnewuser = models.User.objects.values_list('isnewuser', flat=True)
        status_statusid = models.User.objects.values_list('status_statusid', flat=True)
        creados = models.User.objects.values_list('createdat', flat=True)
        mesestrans = models.Transactionpaymentgateway.objects.values_list('creationdatetime', flat=True)
        statustrans = models.Transactionpaymentgateway.objects.values_list('statuspayment_statuspaymentid', flat=True)
        status = graficas.statustrans(statustrans)
        meses= graficas.usuariospormes(creados)
        trans= graficas.usuariospormes(mesestrans)
        trans1= graficas.usuariospormespas(creados)
        vals =graficas.valsuser(isonline,isnewuser,status_statusid)
        companys = models.Company.objects.all()
        productos = models.Product.objects.all()

        return render(request, "index.html",{'vals':vals,'meses':meses,'trans': trans,'trans1': trans1,'statustrans': status,'productos': productos,})
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))