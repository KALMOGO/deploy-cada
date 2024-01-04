# Generated by Django 4.1.4 on 2023-12-24 01:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AlerteInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.CharField(max_length=250)),
                ("date_debut", models.DateTimeField(verbose_name="Date de debut")),
                ("date_fin", models.DateTimeField(verbose_name="Date de fin")),
                (
                    "created_at",
                    models.DateTimeField(auto_now=True, verbose_name="Date d'ajout"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Derniere modification"
                    ),
                ),
                ("slug", models.SlugField(max_length=1000)),
            ],
            options={
                "ordering": ["-created_at", "message"],
            },
        ),
        migrations.CreateModel(
            name="Cada",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=250)),
                ("logo", models.ImageField(upload_to="media/cada/")),
                ("description", tinymce.models.HTMLField()),
                ("slogant", models.CharField(max_length=250)),
                ("cover_image", models.ImageField(upload_to="media/cada/")),
                ("mission", models.TextField()),
                ("vision", models.TextField()),
                ("valeur", models.TextField()),
                ("tel", models.CharField(max_length=25)),
                ("tel2", models.CharField(max_length=25)),
                ("email", models.EmailField(max_length=254)),
                ("facebook", models.CharField(max_length=250)),
                ("date_creation", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-date_creation", "nom"],
            },
        ),
        migrations.CreateModel(
            name="CategorieActualite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("intitule", models.CharField(max_length=250)),
                ("date_creation", models.DateTimeField(auto_now=True)),
                ("slug", models.SlugField(max_length=255)),
            ],
            options={
                "ordering": ["-date_creation", "intitule"],
            },
        ),
        migrations.CreateModel(
            name="DocumentUtile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("intitule", models.CharField(max_length=250)),
                (
                    "fichier",
                    models.FileField(max_length=255, upload_to="media/documents/"),
                ),
                ("annee", models.IntegerField()),
                ("date_creation", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-annee"],
            },
        ),
        migrations.CreateModel(
            name="LienUtile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("intitule", models.CharField(max_length=250)),
                ("lien", models.TextField()),
                ("date_creation", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Partenaire",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "intitule",
                    models.CharField(
                        max_length=250, verbose_name="Denommination du partenaire"
                    ),
                ),
                ("logo", models.ImageField(upload_to="media/partners/")),
                ("date_creation", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Personnel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=250)),
                ("prenom", models.CharField(max_length=250)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("grade", models.CharField(max_length=250)),
                ("poste", models.CharField(max_length=250)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="media/teams/",
                        verbose_name="Image de profil",
                    ),
                ),
                ("date_creation", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-date_creation", "nom", "prenom"],
            },
        ),
        migrations.CreateModel(
            name="Phototheque",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("intitule", models.CharField(max_length=250)),
                ("image", models.ImageField(upload_to="media/photo/")),
                ("date_creation", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("intitule", models.CharField(max_length=50)),
                ("cover_image", models.ImageField(upload_to="media/project/")),
                ("description", tinymce.models.HTMLField()),
                (
                    "resume",
                    models.CharField(
                        max_length=250, verbose_name="Resume de lapublication"
                    ),
                ),
                ("date_creation", models.DateTimeField(auto_now=True)),
                ("slug", models.SlugField(max_length=255)),
            ],
            options={
                "ordering": ["-date_creation", "intitule"],
            },
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("cover_image", models.ImageField(upload_to="media/service/")),
                ("date_creation", models.DateTimeField(auto_now=True)),
                ("description", tinymce.models.HTMLField()),
                ("slug", models.SlugField(max_length=255)),
            ],
            options={
                "ordering": ["-date_creation", "name"],
            },
        ),
        migrations.CreateModel(
            name="Visite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ip_addr", models.CharField(max_length=17, verbose_name="Adresse IP")),
                ("page", models.CharField(max_length=20, verbose_name="Page")),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="CoveredImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="media/coveredImages/")),
                ("title", models.CharField(max_length=250, verbose_name="Titre")),
                (
                    "subTitle",
                    models.CharField(max_length=250, verbose_name=" Sous Titre"),
                ),
                (
                    "description",
                    models.CharField(max_length=250, verbose_name="Description"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Date de Creation"
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="imageCovered",
                        to="main.service",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Actualite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("intitule", models.CharField(max_length=50)),
                ("cover_image", models.ImageField(upload_to="media/actualite/")),
                ("description", tinymce.models.HTMLField()),
                (
                    "resume",
                    models.CharField(
                        max_length=250, verbose_name="Resume de lapublication"
                    ),
                ),
                ("date_creation", models.DateTimeField(auto_now=True)),
                ("slug", models.SlugField(max_length=255)),
                (
                    "auteur",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="actualites",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "categorie",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="actualites",
                        to="main.categorieactualite",
                    ),
                ),
            ],
            options={
                "ordering": ["-date_creation", "intitule"],
            },
        ),
        migrations.CreateModel(
            name="DocumentProject",
            fields=[
                (
                    "documentutile_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="main.documentutile",
                    ),
                ),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.project"
                    ),
                ),
            ],
            bases=("main.documentutile",),
        ),
        migrations.CreateModel(
            name="DocumentActualite",
            fields=[
                (
                    "documentutile_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="main.documentutile",
                    ),
                ),
                (
                    "actualite",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.actualite"
                    ),
                ),
            ],
            bases=("main.documentutile",),
        ),
    ]
