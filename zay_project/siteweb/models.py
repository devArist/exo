from django.db import models

# Create your models here.
class BaseField(models.Model):

    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default = True)

    class Meta:
        abstract = True

class Slider(BaseField):

    color = models.BooleanField(default = False ,verbose_name = 'couleur')
    title = models.CharField(max_length=250,verbose_name = 'titre')
    subtitle = models.CharField(max_length=250,verbose_name = 'sous-titre')
    description = models.TextField()
    image = models.FileField(upload_to='images')

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'

    def __str__(self):
        return self.title
    



class Sociaux(BaseField):

    name = models.CharField(max_length=250,verbose_name = 'nom')
    icon = models.CharField(max_length=250,verbose_name = 'icone')
    lien = models.CharField(max_length=250)
    

    class Meta:
        verbose_name = 'reseau social'
        verbose_name_plural = 'reseaux sociaux'

    def __str__(self):
        return self.name


class SiteWeb(BaseField):

    name = models.CharField(max_length=250,verbose_name = 'nom du site')
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    copyrighte = models.CharField(max_length=250,verbose_name = 'copyright')
    description_category = models.TextField()
    description_product = models.TextField()
    

    class Meta:
        verbose_name = 'site web'
        verbose_name_plural = 'site web'

    def __str__(self):
        return self.name


class About(BaseField):

    image = models.FileField(upload_to='images')
    description_about = models.TextField()
    description_service = models.TextField()
    description_marque = models.TextField()
    

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'

    def __str__(self):
        return self.creat_at


class Newletter(BaseField):

    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name = 'email'
        verbose_name_plural = 'emails'

    def __str__(self):
        return self.email


class Contact(BaseField):
    
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

    def __str__(self):
        return self.name