from django.contrib import admin
from . import models

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    
    list_display = ('name','creat_at','update_at','status')

class ArticleInline(admin.StackedInline):
    model = models.Article
    extra = 1

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ('name','creat_at','update_at','status')

@admin.register(models.Star)
class StarAdmin(admin.ModelAdmin):
    
    list_display = ('user','note','creat_at','update_at','status')

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    
    list_display = ('genre','creat_at','update_at','status')

@admin.register(models.GroupCategorie)
class GroupCategorieAdmin(admin.ModelAdmin):
    
    list_display = ('name','creat_at','update_at','status')

@admin.register(models.CategorieArticle)
class CategorieArticleAdmin(admin.ModelAdmin):
    
    list_display = ('name','creat_at','update_at','status')
    inlines = [ArticleInline]

# Register your models here.
