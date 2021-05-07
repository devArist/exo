from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
    
    list_display = ('title','creat_at','update_at','status')


@admin.register(models.Sociaux)
class SociauxAdmin(admin.ModelAdmin):
    
    list_display = ('name','creat_at','update_at','status')


@admin.register(models.SiteWeb)
class SiteWebAdmin(admin.ModelAdmin):
    
    list_display = ('name','email','phone','address','creat_at','update_at','status')


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    
    list_display = ('creat_at','update_at','status')

@admin.register(models.Newletter)
class NewletterAdmin(admin.ModelAdmin):
    
    list_display = ('email','creat_at','update_at','status')

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    
    list_display = ('name','email','subject','creat_at','update_at','status')