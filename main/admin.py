from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([ DocumentUtile, Actualite, AlerteInfo, Visite, Partenaire, LienUtile, Cada, CoveredImage, CategorieActualite, Personnel, DocumentActualite, DocumentProject, Project, Service])