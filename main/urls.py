from django.urls import include, path, re_path
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("project/",project, name="projects"),
    path("team/", team, name="team"),
    path("actualities/", actualities, name="actualities"),
    path("services/", services, name="services"),
    path("services/<slug:slug>/", servicesDetails, name="servicesDetail"),
    path("links/", links, name="links"),
    path("documents/", documents, name="doc"),
    path("partenaires/", partenaires, name="partenaires"),
    path("photo/", photo, name="photo"),
    path("actualities/<slug:slug>/", actualitiesDetail, name="actualitiesDetail"),
    path("project/<slug:slug>/", projectDetail, name="projectDetail"),
]