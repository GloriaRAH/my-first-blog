# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):   # Le mot clef spécial class permet d'indiquer que nous sommes en train de définir un objet / Post est le nom de notre modèle / models.Model signifie que Post est un modèle Django
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   # C'est un lien vers un autre modèle
    title = models.CharField(max_length=200)   # Cela nous permet de définir un champ texte avec un nombre limité de caractères
    text = models.TextField()   # Cela nous permet de définir un champ text sans limite de caractères. Parfait pour le contenu d'un blog post, non ?
    created_date = models.DateTimeField(default=timezone.now)   # Définit que le champ en question est une date ou une heure.
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title