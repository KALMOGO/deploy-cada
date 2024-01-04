from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils.text import slugify


# class global 
class DocumentUtile(models.Model):
    intitule = models.CharField(max_length=250)
    fichier = models.FileField( upload_to='media/documents/', max_length=255)
    annee = models.IntegerField()
    date_creation = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-annee"]

    def __str__(self) -> str:
        return f"{self.intitule}"

# Personnal(Membre de l'equipe)
class Personnel(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    email = models.EmailField(max_length=254, null=True, blank=True)
    grade = models.CharField(max_length=250)
    poste = models.CharField(max_length=250)
    image = models.ImageField("Image de profil", upload_to="media/teams/", null=True, blank=True)
    facebook= models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    linkedin= models.CharField(max_length=255, null=True, blank=True)
    date_creation = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255)
    

    class Meta:
        ordering = ["-date_creation", "nom", "prenom"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super(Personnel, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.image} {self.grade} {self.nom} {self.prenom} {self.poste} {self.email}"



# CADA
class Cada(models.Model):
    nom=models.CharField( max_length=250)
    logo=models.ImageField(upload_to='media/cada/', height_field=None, width_field=None, max_length=None)
    description=HTMLField()
    slogant =  models.CharField(max_length=250)
    cover_image = models.ImageField(upload_to='media/cada/', height_field=None, width_field=None, max_length=None)
    mission = models.TextField()
    vision = models.TextField()
    valeur = models.TextField()
    tel = models.CharField( max_length=25)
    tel2 = models.CharField( max_length=25)
    email = models.EmailField( max_length=254)
    facebook  = models.CharField( max_length=250)
    date_creation = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-date_creation", "nom"]
    
    def __str__(self) -> str:
        return f"{self.nom}"



class Project(models.Model):
    intitule =  models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='media/project/')
    description = HTMLField()
    resume = models.CharField("Resume de lapublication", max_length=250)
    date_creation = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.intitule)
        super(Project, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ["-date_creation", "intitule"]

    def __str__(self) -> str:
        return f"{self.intitule}"


class DocumentProject(DocumentUtile):
    name= models.ForeignKey(Project , on_delete=models.CASCADE)



# Actualite
class CategorieActualite(models.Model):
    intitule=models.CharField(max_length=250)
    date_creation = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.intitule)
        super(CategorieActualite, self).save(*args, **kwargs)
        
    class Meta:
        ordering = ["-date_creation", "intitule"]

    def __str__(self) -> str:
        return f"{self.intitule}"


class Actualite(models.Model):
    intitule = models.CharField(max_length=550)
    cover_image = models.ImageField(upload_to='media/actualite/')
    description = HTMLField()
    resume = models.CharField("Bref Resumé de l'actualité à afficher avant les détails:", max_length=550)
    auteur = models.ForeignKey(User,on_delete=models.CASCADE, related_name="actualites", blank =True, null =True,)
    categorie = models.ForeignKey(CategorieActualite,on_delete=models.CASCADE, blank =True, null =True, related_name="actualites")
    date_creation = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255)
    date_ofActuality = models.DateField("Date de deroulement de l'actualité",auto_now=False, auto_now_add=False)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.intitule)
        super(Actualite, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ["-date_creation", "intitule"]

    def __str__(self) -> str:
        return f"{self.intitule}"
    
class DocumentActualite(DocumentUtile):
    actualite = models.ForeignKey(Actualite , on_delete=models.CASCADE)


class Service(models.Model):
    
    name = models.CharField(max_length=250)
    cover_image = models.ImageField(upload_to='media/service/')
    date_creation = models.DateTimeField(auto_now=True)
    description = HTMLField("Description detaillé du service")
    brefDescription = models.CharField("description à affiche avant les détail",max_length=250, blank=True, null =True )
    slug = models.SlugField(max_length=255)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Service, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ["-date_creation", "name"]
    
    def __str__(self):
        return f"{self.name}"

class LienUtile(models.Model) :
    intitule = models.CharField(max_length=250, )
    lien = models.TextField()
    date_creation = models.DateTimeField( auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.intitule}"


class Partenaire (models.Model) :
    intitule = models.CharField("Denommination du partenaire", max_length=250)
    logo = models.ImageField(upload_to="media/partners/")
    date_creation = models.DateTimeField( auto_now=True)
    site = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255)

    def __str__(self) -> str:
        return f"{self.intitule}"
    
    
class Phototheque (models.Model) :
    intitule = models.CharField( max_length=250)
    image = models.ImageField(upload_to="media/photo/")
    date_creation = models.DateTimeField( auto_now=True)
    slug = models.SlugField(max_length=255)



# Actualite
class AlerteInfo (models.Model) :
    message=models.CharField(max_length=250)
    date_debut = models.DateTimeField("Date de debut")
    date_fin = models.DateTimeField("Date de fin")
    created_at = models.DateTimeField("Date d'ajout", auto_now=True)
    updated_at = models.DateTimeField("Derniere modification", auto_now_add=True)
    slug = models.SlugField(max_length=1000)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.message)
        super(AlerteInfo, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ["-created_at", "message"]



class Visite (models.Model) :
    ip_addr = models.CharField("Adresse IP", max_length=17)
    page = models.CharField("Page", max_length=20)
    created_at = models.DateTimeField(auto_now=True)



class CoveredImage(models.Model) :
    
    image = models.ImageField(upload_to="media/coveredImages/")
    title = models.CharField("Titre" ,max_length=250)
    subTitle    = models.CharField(" Sous Titre", max_length=250)
    description = models.CharField('Description' ,max_length=250)
    service     = models.ForeignKey(Service, on_delete=models.CASCADE, related_name = 'imageCovered')
    created_at  = models.DateTimeField("Date de Creation", auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self) -> str:
        return self.title