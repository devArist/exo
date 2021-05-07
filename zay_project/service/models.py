from django.db import models
from django.contrib.auth.models import User
from siteweb.models import BaseField

# Create your models here.

class Service(BaseField):
    icon = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def __str__(self):
        return self.name


class Article(BaseField):
    image = models.FileField(upload_to='images')
    name = models.CharField(max_length=200)
    prix = models.FloatField()
    category = models.ForeignKey(
        "service.CategorieArticle", 
        verbose_name="CategorieArticle", 
        on_delete=models.CASCADE, 
        related_name='article_category'
        )
    genre = models.ManyToManyField(
        "service.Genre", 
        verbose_name="genre", 
        related_name='article_genre'
        )
    taille = models.ManyToManyField("service.Taille", related_name='article_taille')
    pointure = models.ManyToManyField("service.Pointure", related_name='article_pointure')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.name


class Star(BaseField):
    user = models.OneToOneField(User, verbose_name=("utlisateur"), on_delete=models.CASCADE)
    note = models.IntegerField()
    article = models.ForeignKey("service.Article", verbose_name=("article a noté "), on_delete=models.CASCADE, related_name='article_stars')

    class Meta:
        verbose_name = 'star'
        verbose_name_plural = 'stars'

    def __str__(self):
        return self.user

class Genre(BaseField):
    CHOICES = [
        ('H', 'Hommes'),
        ('F', 'Femmes'),
        ('HF', 'All')
    ]
    genre = models.CharField(max_length=50, choices=CHOICES, default='HF')

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def __str__(self):
        return self.genre


class GroupCategorie(BaseField):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'groupe de categorie'
        verbose_name_plural = 'groupe de categories'

    def __str__(self):
        return self.name

class CategorieArticle(BaseField):
    name = models.CharField(max_length=50)
    category = models.ForeignKey("service.GroupCategorie", verbose_name=("groupe"), on_delete=models.CASCADE, related_name='groupe_article')
    class Meta:
        verbose_name = 'categorie article'
        verbose_name_plural = 'categorie articles'

    def __str__(self):
        return self.name


class Taille(BaseField):
    name = models.CharField(max_length=10, verbose_name='nom', blank=True, null=True)


class Pointure(BaseField):
    valeur = models.IntegerField(verbose_name='valeur', blank=True, null=True)