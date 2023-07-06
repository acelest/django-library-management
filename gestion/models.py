from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Livre(models.Model):
    nom = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100)
    pages = models.IntegerField()
    image = models.ImageField(upload_to='book_image', blank=True, null=True)

    def __str__(self):
        return self.nom


class User(AbstractUser):
    ville = models.CharField(max_length=100)
    age = models.IntegerField()
    sexe = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    photo = models.ImageField(upload_to='profile_image', blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='gestion_users'  
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='gestion_users'  
    )

    def __str__(self):
        return self.username
