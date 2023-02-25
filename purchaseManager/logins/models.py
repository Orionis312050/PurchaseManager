from django.db import models


# Create your models here.
class User(models.Model):
    pseudo = models.CharField(max_length=200)
    email = models.EmailField()
    mdp = models.CharField(max_length=50)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return self.pseudo
