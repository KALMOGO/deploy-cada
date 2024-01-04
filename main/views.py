from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from datetime import datetime, date,timedelta
import os
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def set_visite (request, page) :
    # compter le nombre de visiteurs
    
    now = datetime.now()
    format_date = "%Y-%m-%d %H:%M:%S.%f"
    # print(request.session["visite_date"])
    if not request.session.get("visite") :
        request.session["visite"] = True
        request.session["visite_date"] = str(now)
        
        ip_addr = request.META.get('REMOTE_ADDR', None)
        Visite.objects.create(
            ip_addr = str(ip_addr),
            page = page
        )
    elif (now - datetime.strptime(request.session["visite_date"], format_date)) >= timedelta(hours=1) :
        print("")
        request.session["visite"] = True
        request.session["visite_date"] = str(now)
        ip_addr = request.META.get('REMOTE_ADDR', None)
        Visite.objects.create(
            ip_addr = str(ip_addr),
            page = page
        )
        

def home(request):
    
    # set a visite et nombre
    set_visite(request, "home")
    today = date.today()
    current_month = today.month
    current_year = today.year
    
    context = {
        'active_tab':'home',
        'coveredImage':CoveredImage.objects.all(),
        "view_today" : Visite.objects.filter(created_at__date=today).count(),
        "view_all" : Visite.objects.all().count(),
        "view_year" : Visite.objects.filter(created_at__year=current_year).count(),
        'alertInfo' :  AlerteInfo.objects.filter(date_debut__lte=datetime.now(), date_fin__gte=datetime.now()),
        "partners" :  Partenaire.objects.all(),
        "recentActualities" : Actualite.objects.all().order_by('id')[:3] # les trois actualités les plus recent
    }
    return  render(request, 'index.html', context)

def actualities(request):
    context = {'active_tab': 'actualities'}
    
    return render(request, 'actualite.html', context=context)


def team(request):
    context={
        'active_tab': 'team',
        'personnel_list': Personnel.objects.all()
    }
    return render(request, 'equipe.html', context)


def project(request):
    context = {
        'active_tab': 'project',
        'project_list': Project.objects.all()
    }
    return render(request, 'projet.html', context)


def services(request):
    services_list = Service.objects.all()
    paginator = Paginator(Service.objects.all(), 3)
    page = request.GET.get('page')

    page = request.GET.get('page')

    try:
        services = paginator.page(page)
    except PageNotAnInteger:
        services = paginator.page(1)
    except EmptyPage:
        services = paginator.page(paginator.num_pages)
    
    context = {
        'active_tab': 'Services',
        'services_list': services
    }

    return render(request, 'services.html', context)

def servicesDetails(request, slug):
    service = get_object_or_404(Service, slug=slug)
    context = {
        'active_tab': 'servicesDetails',
        'service': service
    }
    return render(request, 'service-single.html', context)

def links(request):
    context = {
        'links' : LienUtile.objects.all()
    }
    return render(request, 'lienUtile.html', context)


def documents(request):
    context = {'active_tab': 'documents'}
    return render(request, 'documentUtile.html', context)


def photo(request):
    photos_list = Phototheque.objects.all()
    paginator = Paginator(photos_list, 4)
    page = request.GET.get('page')

    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)
    
    context = {
        'active_tab': 'photo',
        'photos_list': photos
    }
    return render(request, 'phototheque.html', context)


def partenaires(request):
    partenaires_list = Partenaire.objects.all()
    paginator = Paginator(partenaires_list, 4)
    page = request.GET.get('page')

    try:
        partenaires = paginator.page(page)
    except PageNotAnInteger:
        partenaires = paginator.page(1)
    except EmptyPage:
        partenaires = paginator.page(paginator.num_pages)
    
    context = {'active_tab': 'partenaires', 'partenaires_list': partenaires}
    return render(request, 'partenaires.html', context)

def page_non_trouvee(request, exception):
    return render(request, 'erreur_404.html', status=404)

def erreur_serveur(request):
    return render(request, 'erreur_500.html', status=500)


def pdf_view(request, path):
    with open(path, 'rb') as pdf_file:
        response = FileResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{os.path.basename(path)}"'
    return response


def actualitiesDetail(request, slug):
    context = {}
    return render(request, 'actualite-single.html', context=context)


def projectDetail(request, slug):
    projet = get_object_or_404(Project, slug=slug)
    context = {'projet': projet}
    return render(request, 'project-single.html', context=context)
    
